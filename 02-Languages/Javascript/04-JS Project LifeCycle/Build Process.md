## Modern Project Characteristics

- Version control

- Automated CI/CD

- Code Quality

- Tooling

- Module support for ES module

- Documented API

- Demos

  

## Build Process

- Automated sequences of tasks that runs on each push, tag or release.

 - install

 - clean install `npm ci`

 - security audit `npm audit`

 - lint (Code Quality some automated coding pattern)

 - linter `eslint`/`stylelint`

 - formatter `prettier`

 - test

 - test suite `jest`/`mocha`/`ava`

 - code coverage `nyc`/`codecov`/`coveralls`

 - build

 - transpile `babel`/`typescript`/`flow`

 - pre-process(compile, auto-prefix etc) `sass`/`less`/`postcss`

 - uglify (minify, mingle, optimize etc) `uglify.js`/`terser`

 - bundle(concat, tree-shake etc) `webpack`/`rollup`/`parcel`

 - compress (gzip etc)

 - other tasks

 - copy/ delete/ move files

 - check bundle size

 - strip unused code (ts/flow/prototypes)

 - push

 - release `github`

 - publish `npm`

 - deploy

 - host `heroku`

  

## Task Execution

- CLI `npm`

- task runner `grunt`, `gulp`, `brunch` **CLI prefered now**