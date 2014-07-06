# The Chrome DevTools documentation

This is the source of the official [DevTools documentation](https://developer.chrome.com/devtools/index) on developer.chrome.com (aka "DCC").



## Contributing

We regularly update the docs and welcome any contributions or bug-fixes.

Before submitting a pull request, please open a [new issue](https://github.com/GoogleChrome/devtools-docs/issues/new) to let us know you're working on.

This will allow us to provide feedback and coordinate contribution efforts.

FYI The extension docs live in the chromium repo: `chromium/src/chrome/common/extensions/docs`

### Orientation

<dl>
  <dt> ./docs </dt>
  <dd> Contains all the working files. </dd>

  <dt> ./index.html </dt>
  <dd> Contains the project <a href="https://developer.chrome.com/devtools/index">overview</a> page. </dd>

  <dt> ./images </dt>
  <dd> Contains images for index.html. </dd>

  <dt> ./_book.yaml </dt>
  <dd> Contains the titles and paths of individual docs. </dd>

  <dt> ./_redirect.yaml </dt>
  <dd> Contains redirects from one location to another. </dd>

</dl>

### Additional DevTools docs

Covered in the [DevTools Content Inventory](https://github.com/GoogleChrome/devtools-docs/wiki/Content-Inventory)

### Running the site

1. In the root of the project, start a [server] (https://github.com/paulirish/dotfiles/blob/3fa2e7dc1f1ea5eaf7f6a2531b937ff8bd8833f9/.functions#L25-L32).
  * It's easier if your server can also do a directory listing.
1. Open [http://localhost:8000/docs/_preview.html](http://localhost:8000/docs/_preview.html)
1. You will see the boilerplate along with a directory listing ![image](https://cloud.githubusercontent.com/assets/39191/3017501/7e6985da-df7a-11e3-9a7c-51f964906839.png)
1. Click one of them.
1. It should bring you to a url like [http://localhost:8000/docs/_preview.html?settings.html](http://localhost:8000/docs/_preview.html?settings.html)
  * you can navigate to this directly if you like
  * it looks like this ![image](https://cloud.githubusercontent.com/assets/39191/3017506/831921a8-df7a-11e3-8faa-8dc957057248.png)
  * Things mostly work but is not exactly the same as viewing through DCC.

### Deployment

Once pushed to master, updates will go live to the DCC site within a few minutes or so.

#### Troublshooting
* Make sure you've created CLs with any imported GH changes. 
* If you can't find the content with the devtools-docs repo, it might be part of the Chromium repo
  * CSS, JavaScript, and navigation bugs related to developer.chrome.com can be logged to the [Chromium issue tracker](http://crbug.com) 

## License

Except as otherwise noted, the content of the DevTools documentation is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0).


## Crxdoczh Specifics

Some files are removed:

    docs/boilerplate_files/developers-logo-footer.png
    docs/boilerplate_files/developers-logo.svg
    docs/boilerplate_files/format+en,default,table.I.js
    docs/boilerplate_files/local_extensions.css
    docs/boilerplate_files/marked.js
    docs/boilerplate_files/preview.js
    docs/boilerplate_files/screen.css
    docs/boilerplate_files/search.png
    docs/boilerplate_files/table.css
    docs/elements-styles-files/blackSuggest.png
    docs/elements-styles-files/borderSuggest.png
    docs/elements-styles-files/computedStyles.png
    docs/elements-styles-files/disabledProperty.png
    docs/elements-styles-files/gear.png
    docs/elements-styles-files/magnifier.png
    docs/elements-styles-files/metrics.png
    docs/elements-styles-files/pseudoInherited.png
    docs/elements-styles-files/ruleDiff.png
    docs/elements-styles-files/tutorial.css
    docs/elements-styles-files/warningIcon.png
    docs/elements-styles.html
    docs/elements.html
    docs/rendering-settings-files/composited-layer-borders.png
    docs/rendering-settings-files/continuous-page-repainting.png
    docs/rendering-settings-files/fps-memory-meter.png
    docs/rendering-settings-files/fps-meter.png
    docs/rendering-settings-files/rendering-settings.png
    docs/rendering-settings-files/show-paint-rects.png
    docs/rendering-settings.html
    docs/scripts-exceptions-files/examples.js
    docs/tests/xhr-test.html
    pillar-images/console-pillar.png
    pillar-images/cpuprofiler-pillar.png
    pillar-images/dom-pillar.png
    pillar-images/emulation-pillar.png
    pillar-images/flamechart-pillar.png
    pillar-images/jsdebugger-pillar.png
    pillar-images/memory-pillar.png
    pillar-images/remote-debugging-pillar.jpg
    pillar-images/shortcuts-pillar.JPG
    pillar-images/timeline-pillar.png
    pillar.html
