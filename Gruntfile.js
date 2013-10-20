module.exports = function(grunt) {
    var modules = {
        self: this,
        grunt: grunt
    };

    grunt.initConfig({
            jshint: {
                options: {
                },
                // Don't inlclude app/js/lib_viewer or app/js/moxie here.
                all: [
                    'Gruntfile.js',
                    'app/js/*.js',
                    'app/js/controllers/**/*.js',
                    'app/js/directives/**/*.js',
                    'app/js/filters/**/*.js',
                    'app/js/services/**/*.js',
                    'app/js/tests/**/*.js',
                    'app/js/viewing/**/*.js'
                ]
            },

            requirejs: {

                development: {
                    options: {
                        baseUrl:        "app/",
                        mainConfigFile: "app/main.js",
                        out:            "app/built_app.js",
                        name:           "main",
                        paths:          {
                            requireLib: 'js/lib/require'
                        },
                        include:        'requireLib',
                        optimize:       'uglify2',
                        generateSourceMaps: true,
                        preserveLicenseComments: false,
                        useSourceUrl: true
                    }
                }
            }
        }
    );

    grunt.loadNpmTasks('grunt-contrib-copy');
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-jsdoc');
    grunt.loadNpmTasks('grunt-karma');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('default', ['jshint',
                                   'requirejs:development']);
};

