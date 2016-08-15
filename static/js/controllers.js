/**
 * INSPINIA - Responsive Admin Theme
 *
 */

/**
 * MainCtrl - controller
 */
function MainCtrl() {

    this.userName = 'Кутылев С.А.';
    this.helloText = 'Добро пожаловать на Внутренний портал ФКН ВШЭ';
    this.descriptionText = 'It is an application skeleton for a typical AngularJS web app. You can use it to quickly bootstrap your angular webapp projects and dev environment for these projects.';

};


angular
    .module('inspinia')
    .controller('MainCtrl', MainCtrl)