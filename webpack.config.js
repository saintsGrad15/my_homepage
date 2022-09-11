import path from path;

module.exports = {
    module: {
        rules: [
            {
                test: /\.(json)$/i,
                type: 'assets',
            }
        ]
    },
    resolve: {
        alias: {
            "@": path.resolve("__dirname", "src")
        }
    }
};