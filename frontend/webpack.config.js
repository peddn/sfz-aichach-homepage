const path = require('path');

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const RemovePlugin = require('remove-files-webpack-plugin');
const CopyPlugin = require("copy-webpack-plugin");

module.exports = {
    // https://stackoverflow.com/questions/35903246/how-to-create-multiple-output-paths-in-webpack-config
    entry: {
        'main/static/bundle': './main/js/main.js',
        'home/static/bundle': './home/js/main.js'
    },
    output: {
        path: path.resolve(__dirname, '../backend'),
        filename: '[name].js'
    },
    module: {
        rules: [
            {
                test: /\.scss$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    {
                        loader: 'css-loader'
                    },
                    {
                        loader: 'sass-loader'
                    }
                ]
            }
        ]
    },
    plugins: [
        new RemovePlugin({
            before: {
                root: '../backend',
                include: [
                    'main/static',
                    'main/templates',
                    'home/static',
                    'home/templates',
                    'search/templates'
                ],
                log: true,
                recursive: true
            },
            watch: {
                // parameters for "before watch compilation" stage.
            },
            after: {
                // parameters for "after normal and watch compilation" stage.
            }
        }),
        new CopyPlugin({
            patterns: [
                { from: './main/templates', to: '../backend/main/templates', force: true },
                { from: './home/templates', to: '../backend/home/templates', force: true },
                { from: './search/templates', to: '../backend/search/templates', force: true },
                {
                    from: './assets', to: '../backend/main/static/assets', force: true,
                    globOptions: {
                        ignore: [
                            // Ignore all subdirectories called 'src'
                            "**/src",
                        ],
                    }
                }
            ],
            options: {}
        }),
        new MiniCssExtractPlugin({
            filename: '[name].css'
        })
    ]
};

