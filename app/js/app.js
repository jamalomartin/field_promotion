define([
    'angular',
    'js/controllers/controllers',
    'js/filters/filters',
    'js/services/services',
    'js/directives/directives'
], function(angular){
        'use strict';

        var app =  angular.module('FieldPromotion', ['controllers', 'services', 'filters', 'directives']);
        console.log('test');
        app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider){
            $locationProvider.html5Mode(true);
            $routeProvider.
                when('/', {templateUrl: 'templates/record_game.html', controller: 'RecordGameController'}).
                when('/admin', {templateUrl: 'templates/admin.html', controller: 'AdminController'}).
                when('/record', {templateUrl: 'templates/record_game.html', controller: 'RecordGameController'}).
                when('/view', {templateUrl: 'templates/view_game.html', controller: 'GameResultsController'});
        }]);

        return app;
    }
);
