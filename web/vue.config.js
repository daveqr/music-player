const path = require('path');

module.exports = {
  transpileDependencies: true,
  chainWebpack: (config) => {
    config.plugin('html').tap((args) => {
      args[0].title = 'My Music App';
      return args;
    });

    config.resolve.alias.set('@', path.resolve(__dirname, 'src'));
  },
};
