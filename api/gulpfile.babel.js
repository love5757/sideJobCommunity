'use strict';

import gulp from 'gulp';
import gutil from 'gulp-util';
import uglify from 'gulp-uglify-es';
import cleanCSS from 'gulp-clean-css';
import htmlmin from 'gulp-htmlmin';
import del from 'del';
// import spawn from 'child_process';

var spawn = require('child_process').spawn;

const DIR = {
    SRC: 'api',
    DEST: 'dist'
};

const SRC = {
    JS: DIR.SRC + '/**/**.js',
    CSS: DIR.SRC + '/**.css',
    HTML: DIR.SRC + '/**.html'
};

const DEST = {
    JS: DIR.DEST + '/js',
    CSS: DIR.DEST + '/css',
    HTML: DIR.DEST + '/'
};


gulp.task('js', () => {
    return gulp.src(SRC.JS)
           .pipe(uglify())
           .pipe(gulp.dest(DEST.JS));
});

gulp.task('css', () => {
    return gulp.src(SRC.CSS)
           .pipe(cleanCSS({compatibility: 'ie8'}))
           .pipe(gulp.dest(DEST.CSS));
});

gulp.task('html', () => {
    return gulp.src(SRC.HTML)
          .pipe(htmlmin({collapseWhitespace: true}))
          .pipe(gulp.dest(DEST.HTML))
});

gulp.task('clean', (done) => {
    del.sync([DIR.DEST]);
    done();
});

gulp.task('default', gulp.series('clean', 'js', 'css', 'html', (done) => {
    gutil.log('Gulp is running');
    done();
}));

gulp.task('serve', (done) => {
    const spawnOptions = {
        shell: true,
        stdio: 'inherit',
      };
    spawn('npm', ['start'], spawnOptions);
    done();
});