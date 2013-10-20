
define([
    'angular'
],  function(
    angular
    ) {
    "use strict";

    var GameResultsController = function ($scope){
        $scope.test = 'GameResultsController';
    };

    GameResultsController.$inject = [
        '$scope'
    ];

    return GameResultsController;
});
