/**
 * INSPINIA - Responsive Admin Theme
 *
 * Inspinia theme use AngularUI Router to manage routing and views
 * Each view are defined as state.
 * Initial there are written state for all view in theme.
 *
 */
function config($stateProvider, $urlRouterProvider, $ocLazyLoadProvider, $httpProvider, $interpolateProvider) {

    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $urlRouterProvider.otherwise("/index/main");

    $ocLazyLoadProvider.config({
        // Set to true if you want to see what and when is dynamically loaded
        debug: false
    });

    $stateProvider

        .state('index', {
            abstract: true,
            url: "/index",
            templateUrl: "/static/templates/views/common/content.html",
        })
        .state('index.main', {
            url: "/main",
            templateUrl: "/static/templates/views/main.html",
            data: { pageTitle: 'Главная' }
        })
        .state('index.calendar', {
            url: "/calendar",
            templateUrl: "/static/templates/views/calendar.html",
            data: { pageTitle: 'Календарь отсутствий' }
        })
        .state('index.science', {
            url: "/science",
            templateUrl: "/static/templates/views/science.html",
            data: { pageTitle: 'Наука' }
        })
            .state('index.inform', {
            url: "/inform",
            templateUrl: "/static/templates/views/inform.html",
            data: { pageTitle: 'Информационное совещание' }
        })
            .state('index.collegs', {
            url: "/collegs",
            templateUrl: "/static/templates/views/collegs.html",
            data: { pageTitle: 'Коллегиальные органы' }
        })
            .state('index.empl', {
            url: "/empl",
            templateUrl: "/static/templates/views/empl.html",
            data: { pageTitle: 'Штатное расписание' }
        })
            .state('index.other', {
            url: "/other",
            templateUrl: "/static/templates/views/other.html",
            data: { pageTitle: 'Другое' }
        })

}
angular
    .module('inspinia')
    .config(config)
    .run(function($rootScope, $state) {
        $rootScope.$state = $state;
    });
