
define([
    'angular'
],  function(
    angular
    ) {
    "use strict";

    var AdminController = function ($scope){
        $scope.test = 'AdminController';
    };

    AdminController.$inject = [
        '$scope'
    ];

    return AdminController;
});
