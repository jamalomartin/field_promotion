define([
    'angular',
    'js/controllers/AdminController.js',
    'js/controllers/GameResultsController.js',
    'js/controllers/RecordGameController.js'
], function(
    angular,
    AdminController,
    GameResultsController,
    RecordGameController
    ) {

    "use strict";

    var controllers = angular.module('controllers', []);
    controllers.controller('AdminController', AdminController);
    controllers.controller('GameResultsController', GameResultsController);
    controllers.controller('RecordGameController', RecordGameController);

    return controllers;
});
