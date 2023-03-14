import cv2 #pip install opencv-python
import os

class Header:
    #class data members
    NAME_LENGTH = 20
    SIZE_LENGTH = 10
    HEADER_LENGTH = NAME_LENGTH + SIZE_LENGTH + 8
    PAD_CHAR = '*'

    @classmethod #Invokable without object
    def generate_header(cls, doc):  # doc =  d:/imp_content/secret.docx
        if '/' not in doc:
            raise Exception('Use / as path separator')

        name = doc.split('/')[-1]  # [d:, imp_content, secret.docx]

        l = len(name)
        if l > cls.NAME_LENGTH:
            name = name[l - cls.NAME_LENGTH:]  # trim
        elif l < cls.NAME_LENGTH:
            name = name.rjust(cls.NAME_LENGTH, cls.PAD_CHAR)  # pad

        size = str(os.path.getsize(doc))
        size = size.rjust(cls.SIZE_LENGTH, cls.PAD_CHAR)
        return '$$$$'+ name + size+ '@AIT'

    @classmethod
    def validate_header(cls, header):
        #first 4 characters must be '$$$$'
        #and last 4 characters must be '@AIT'
        ff = header[:4]
        lf = header[len(header)-4:]
        if ff == '$$$$' and lf == '@AIT':
            header = header[4:len(header)-4]
            return header
        else:
            raise Exception('Invalid Header')

class Embeddor:
    #class data
    split_byte_to_bits = lambda data: [data >> 5, (data >> 2) & 0x7, data & 0x3]

    def __init__(self, vessel_image, file_to_embed): #put the object into first state
        #validations
        if not os.path.exists(vessel_image):
            raise Exception(vessel_image, 'doesnt exist') #raise error
        if not os.path.exists(file_to_embed):
            raise Exception(file_to_embed, 'doesnt exist')#raise error

        #preserve the vessel_image and the file_to_embed as attributes of the object
        self.vessel_image = vessel_image
        self.file_to_embed = file_to_embed

    def embed(self):
        # load the image in memory
        mem_image = cv2.imread(self.vessel_image, cv2.IMREAD_COLOR)
        # type(mem_image) --> numpy.ndarray
        # mem_image.shape --> height, width, pixelsize(bgr)
        h, w, _ = mem_image.shape

        # know the size of the document
        doc_size = os.path.getsize(self.file_to_embed)

        # test the embedding capacity
        capacity = h * w

        #error on fail
        if doc_size + Header.HEADER_LENGTH > capacity:
            raise Exception(self.file_to_embed +' too large to fit in' +  self.vessel_image)

        # generate the header
        header = Header.generate_header(self.file_to_embed)

        #generate target name
        target_image = self.generate_embedded_imagename()

        # embed
        cnt = 0
        # open the file for reading in binary mode (to support reading all file types)
        file_handle = open(self.file_to_embed, 'rb')

        flag = True
        i = 0
        while i < h and flag:  # for each row
            j = 0
            while j < w and flag:  # for each col of the row i
                # fetch a pixel
                pixel = mem_image[i, j]
                blue = pixel[0]
                green = pixel[1]
                red = pixel[2]

                if cnt < Header.HEADER_LENGTH:
                    # fetch a byte from the header
                    data = ord(header[cnt])
                else:
                    # fetch a byte from the file
                    data = file_handle.read(1)
                    if data:  # test
                        # data fetched is in the form: byte object
                        # it needs conversion into int
                        data = int.from_bytes(data, byteorder='big')
                    else:
                        # its the EOF
                        flag = False  # stop embedding
                        continue

                bits = Embeddor.split_byte_to_bits(data)

                # embed the bits
                red = (red & (~0x7)) | bits[0]
                green = (green & (~0x7)) | bits[1]
                blue = (blue & (~0x3)) | bits[2]

                # update the mem_image_pixel[i,j]
                mem_image[i, j, 0] = blue
                mem_image[i, j, 1] = green
                mem_image[i, j, 2] = red

                cnt += 1  # next byte
                j += 1  # col change
            i += 1  # row change

        file_handle.close()
        # save back

        cv2.imwrite(target_image, mem_image)
        return target_image

    def generate_embedded_imagename(self):
        # vessel image:- c:/images/kids.jpg
        # embedded image:- c:/images/e_kids.png
        if '/' in self.vessel_image:
            temp = self.vessel_image.split('/')  # ['c:', 'images', 'kids.jpg']
            temp[-1] = 'e_' + temp[-1]  # ['c:', 'images', 'e_kids.jpg']
            ename = '/'.join(temp)  # c:/images/e_kids.jpg
            if ename.lower().endswith('.jpg'):
                ename = ename.replace('.jpg', '.png')
            elif ename.lower().endswith('.jpeg'):
                ename = ename.replace('.jpeg', '.png')
            return ename
        else:
            raise Exception('Use / in ' + self.vessel_image + 'as path separator')


class Extractor:
    #class data
    extract_nbits_of_byte = lambda band, n : band & (2**n-1)
    merge_bits = lambda rbits,gbits, bbits :(((rbits<< 3) | gbits) << 2) | bbits

    def __init__(self, embedded_image, target_folder):
        #validation
        if not os.path.exists(embedded_image):
            raise Exception(embedded_image +'not found')
        if not os.path.exists(target_folder):
            raise Exception(target_folder +  'not found')
        # preserve the embedded_image and the target_folder as attributes of the object
        self.embedded_image = embedded_image
        self.target_folder = target_folder


    def extract(self):
        #load the image in memory
        mem_img = cv2.imread(self.embedded_image, cv2.IMREAD_COLOR)

        #fetch the size
        h,w,_ = mem_img.shape

        flag = True
        i =0
        cnt =0
        header = ''
        while i < h and flag: #for each row
            j =0
            while j < w and flag: #for each col of row i
                #fetch a pixel
                pixel = mem_img[i,j]
                blue = pixel[0]
                green = pixel[1]
                red = pixel[2]

                #extract 3,3,2 bits of the bands (r,g,b) of the pixel
                red_bits = Extractor.extract_nbits_of_byte(red, 3)
                green_bits = Extractor.extract_nbits_of_byte(green, 3)
                blue_bits = Extractor.extract_nbits_of_byte(blue, 2)

                #merge the bits to form the byte
                data = Extractor.merge_bits(red_bits, green_bits, blue_bits)

                if cnt < Header.HEADER_LENGTH:
                    header = header + chr(data)
                else:
                    if cnt == Header.HEADER_LENGTH: #header processing
                        header = Header.validate_header(header)
                        print(header)
                        filename = header[:Header.NAME_LENGTH].strip(Header.PAD_CHAR)
                        filesize = int(header[Header.NAME_LENGTH:].strip(Header.PAD_CHAR))

                        #open the file for writing
                        file_handle = open(self.target_folder+'/'+filename, 'wb')

                    if cnt - Header.HEADER_LENGTH< filesize:
                        #data is a numpy.int
                        #convert it into py int
                        #convert py int into byte object
                        data = int.to_bytes(int(data), 1, byteorder='big')
                        # write to the file (byte objects)
                        file_handle.write(data)
                    else:
                        file_handle.close()
                        flag = False

                cnt+=1
                j+=1
            i+=1
        return  self.target_folder + '/' + filename

def main():
    while True:
        print('1. Embed')
        print('2. Extract')
        print('3. Exit')
        print('Enter Choice ')
        ch = int(input())

        if ch == 1:
            try:
                print('Enter vessel image path')
                vessel_img = input()
                print('Enter file to embed')
                doc = input()
                em = Embeddor(vessel_img, doc)
                result =  em.embed()
                print('Embedding Done, result: ', result)
            except:
                print('Embedding Failed')
        elif ch == 2:
            try:
                print('Enter embedded image path')
                embedded_image = input()
                print('Enter target folder for saving the extracted file')
                target_folder = input()
                ex = Extractor(embedded_image, target_folder)
                result = ex.extract()
                print('Extraction Done, result: ', result)
            except:
                print('Extraction Failed')
        elif ch == 3:
            break
        else:
            print('Wrong Choice')

main()
