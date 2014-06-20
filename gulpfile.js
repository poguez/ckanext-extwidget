var gulp = require('gulp'),
    path = require('path'),
    livereload = require('gulp-livereload');

gulp.task("reload", function () {
    var server = livereload();

    gulp.watch(['template/**']).on('change', function(file) {
        server.changed(file.path);
    });
});



gulp.task('default',["reload"]);
