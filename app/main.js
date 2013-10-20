requirejs.config({
    baseUrl:'./',
    paths:{
        angular: 'js/lib/angular-1.1.5',
        'angular-resource': 'js/lib/angular-resource-1.1.5',
        text: "js/lib/text",
        jquery: "js/lib/jquery-1.9.1",
        lodash: "js/lib/lodash",
    },

    shim: {
        angular: {
            deps: ['jquery'],
            exports: 'angular'
        },
        'angular-resource': {
            deps: ['angular'],
            exports: 'angularResource'
        },
        jquery: {
            exports: '$'
        },
        lodash: {
            exports: '_'
        }
    }
});

if(typeof(console) === 'undefined'){
    console = {};
}

/**
 * The entry point into our stuff.
 */
requirejs(['angular', 'js/app'], function(angular, app){
    "use strict";
    angular.bootstrap(document, ['FieldPromotion']);
});
