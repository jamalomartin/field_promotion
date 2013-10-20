define([
    'angular',
    'js/controllers/controllers',
    'js/filters/filters',
    'js/services/services',
    'js/directives/directives'
], function(angular){
        'use strict';

        var app =  angular.module('FieldPromotion', ['controllers', 'services', 'filters', 'directives']);

        app.config(['$routeProvider', '$locationProvider', 'resourcePath', function($routeProvider, $locationProvider, resourcePath){
            $locationProvider.html5Mode(true);
            $routeProvider.
                when('/', {templateUrl: resourcePath + 'templates/record_game.html', controller: 'RecordGameController'}).
                when('/admin', {templateUrl: resourcePath + 'templates/admin.html', controller: 'AdminController'}).
                when('/record', {templateUrl: resourcePath + 'templates/record_game.html', controller: 'RecordGameController'}).
                when('/view', {templateUrl: resourcePath + 'templates/view_game.html', controller: 'GameResultsController'});
        }]);

        return app;
    }
);
