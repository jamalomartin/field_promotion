
define([
    'angular'
],  function(
    angular
    ) {
    "use strict";

    var RecordGameController = function ($scope){
        $scope.test = 'RecordGameController';
    };

    RecordGameController.$inject = [
        '$scope'
    ];

    return RecordGameController;
});
