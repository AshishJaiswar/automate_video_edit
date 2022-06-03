<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>Create short quote videos using python</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
margin: 0;
padding: 0;
}
@media only screen {
body {
margin: 2em auto;
max-width: 900px;
color: rgb(55, 53, 47);
}
}

body {
line-height: 1.5;
white-space: pre-wrap;
}

a,
a.visited {
color: inherit;
text-decoration: underline;
}

.pdf-relative-link-path {
font-size: 80%;
color: #444;
}

h1,
h2,
h3 {
letter-spacing: -0.01em;
line-height: 1.2;
font-weight: 600;
margin-bottom: 0;
}

.page-title {
font-size: 2.5rem;
font-weight: 700;
margin-top: 0;
margin-bottom: 0.75em;
}

h1 {
font-size: 1.875rem;
margin-top: 1.875rem;
}

h2 {
font-size: 1.5rem;
margin-top: 1.5rem;
}

h3 {
font-size: 1.25rem;
margin-top: 1.25rem;
}

.source {
border: 1px solid #ddd;
border-radius: 3px;
padding: 1.5em;
word-break: break-all;
}

.callout {
border-radius: 3px;
padding: 1rem;
}

figure {
margin: 1.25em 0;
page-break-inside: avoid;
}

figcaption {
opacity: 0.5;
font-size: 85%;
margin-top: 0.5em;
}

mark {
background-color: transparent;
}

.indented {
padding-left: 1.5em;
}

hr {
background: transparent;
display: block;
width: 100%;
height: 1px;
visibility: visible;
border: none;
border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
max-width: 100%;
}

@media only print {
img {
max-height: 100vh;
object-fit: contain;
}
}

@page {
margin: 1in;
}

.collection-content {
font-size: 0.875rem;
}

.column-list {
display: flex;
justify-content: space-between;
}

.column {
padding: 0 1em;
}

.column:first-child {
padding-left: 0;
}

.column:last-child {
padding-right: 0;
}

.table_of_contents-item {
display: block;
font-size: 0.875rem;
line-height: 1.3;
padding: 0.125rem;
}

.table_of_contents-indent-1 {
margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
margin-left: 3rem;
}

.table_of_contents-indent-3 {
margin-left: 4.5rem;
}

.table_of_contents-link {
text-decoration: none;
opacity: 0.7;
border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
border: 1px solid rgba(55, 53, 47, 0.09);
border-collapse: collapse;
}

table {
border-left: none;
border-right: none;
}

th,
td {
font-weight: normal;
padding: 0.25em 0.5em;
line-height: 1.5;
min-height: 1.5em;
text-align: left;
}

th {
color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
margin: 0;
margin-block-start: 0.6em;
margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
margin-block-start: 0.6em;
}

ul > li {
list-style: disc;
}

ul.to-do-list {
text-indent: -1.7em;
}

ul.to-do-list > li {
list-style: none;
}

.to-do-children-checked {
text-decoration: line-through;
opacity: 0.375;
}

ul.toggle > li {
list-style: none;
}

ul {
padding-inline-start: 1.7em;
}

ul > li {
padding-left: 0.1em;
}

ol {
padding-inline-start: 1.6em;
}

ol > li {
padding-left: 0.2em;
}

.mono ol {
padding-inline-start: 2em;
}

.mono ol > li {
text-indent: -0.4em;
}

.toggle {
padding-inline-start: 0em;
list-style-type: none;
}

/_ Indent toggle children _/
.toggle > li > details {
padding-left: 1.7em;
}

.toggle > li > details > summary {
margin-left: -1.1em;
}

.selected-value {
display: inline-block;
padding: 0 0.5em;
background: rgba(206, 205, 202, 0.5);
border-radius: 3px;
margin-right: 0.5em;
margin-top: 0.3em;
margin-bottom: 0.3em;
white-space: nowrap;
}

.collection-title {
display: inline-block;
margin-right: 1em;
}

.simple-table {
margin-top: 1em;
font-size: 0.875rem;
empty-cells: show;
}
.simple-table td {
height: 29px;
min-width: 120px;
}

.simple-table th {
height: 29px;
min-width: 120px;
}

.simple-table-header-color {
background: rgb(247, 246, 243);
color: black;
}
.simple-table-header {
font-weight: 500;
}

time {
opacity: 0.5;
}

.icon {
display: inline-block;
max-width: 1.2em;
max-height: 1.2em;
text-decoration: none;
vertical-align: text-bottom;
margin-right: 0.5em;
}

img.icon {
border-radius: 3px;
}

.user-icon {
width: 1.5em;
height: 1.5em;
border-radius: 100%;
margin-right: 0.5rem;
}

.user-icon-inner {
font-size: 0.8em;
}

.text-icon {
border: 1px solid #000;
text-align: center;
}

.page-cover-image {
display: block;
object-fit: cover;
width: 100%;
max-height: 30vh;
}

.page-header-icon {
font-size: 3rem;
margin-bottom: 1rem;
}

.page-header-icon-with-cover {
margin-top: -0.72em;
margin-left: 0.07em;
}

.page-header-icon img {
border-radius: 3px;
}

.link-to-page {
margin: 1em 0;
padding: 0;
border: none;
font-weight: 500;
}

p > .user {
opacity: 0.5;
}

td > .user,
td > time {
white-space: nowrap;
}

input[type="checkbox"] {
transform: scale(1.5);
margin-right: 0.6em;
vertical-align: middle;
}

p {
margin-top: 0.5em;
margin-bottom: 0.5em;
}

.image {
border: none;
margin: 1.5em 0;
padding: 0;
border-radius: 0;
text-align: center;
}

.code,
code {
background: rgba(135, 131, 120, 0.15);
border-radius: 3px;
padding: 0.2em 0.4em;
border-radius: 3px;
font-size: 85%;
tab-size: 2;
}

code {
color: #eb5757;
}

.code {
padding: 1.5em 1em;
}

.code-wrap {
white-space: pre-wrap;
word-break: break-all;
}

.code > code {
background: none;
padding: 0;
font-size: 100%;
color: inherit;
}

blockquote {
font-size: 1.25em;
margin: 1em 0;
padding-left: 1em;
border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
text-decoration: none;
max-height: 8em;
padding: 0;
display: flex;
width: 100%;
align-items: stretch;
}

.bookmark-title {
font-size: 0.85em;
overflow: hidden;
text-overflow: ellipsis;
height: 1.75em;
white-space: nowrap;
}

.bookmark-text {
display: flex;
flex-direction: column;
}

.bookmark-info {
flex: 4 1 180px;
padding: 12px 14px 14px;
display: flex;
flex-direction: column;
justify-content: space-between;
}

.bookmark-image {
width: 33%;
flex: 1 1 180px;
display: block;
position: relative;
object-fit: cover;
border-radius: 1px;
}

.bookmark-description {
color: rgba(55, 53, 47, 0.6);
font-size: 0.75em;
overflow: hidden;
max-height: 4.5em;
word-break: break-word;
}

.bookmark-href {
font-size: 0.75em;
margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
color: rgba(55, 53, 47, 1);
}
.highlight-gray {
color: rgba(120, 119, 116, 1);
fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
color: rgba(159, 107, 83, 1);
fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
color: rgba(217, 115, 13, 1);
fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
color: rgba(203, 145, 47, 1);
fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
color: rgba(68, 131, 97, 1);
fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
color: rgba(51, 126, 169, 1);
fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
color: rgba(144, 101, 176, 1);
fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
color: rgba(193, 76, 138, 1);
fill: rgba(193, 76, 138, 1);
}
.highlight-red {
color: rgba(212, 76, 71, 1);
fill: rgba(212, 76, 71, 1);
}
.highlight-gray_background {
background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
background: rgba(253, 235, 236, 1);
}
.block-color-default {
color: inherit;
fill: inherit;
}
.block-color-gray {
color: rgba(120, 119, 116, 1);
fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
color: rgba(159, 107, 83, 1);
fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
color: rgba(217, 115, 13, 1);
fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
color: rgba(203, 145, 47, 1);
fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
color: rgba(68, 131, 97, 1);
fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
color: rgba(51, 126, 169, 1);
fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
color: rgba(144, 101, 176, 1);
fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
color: rgba(193, 76, 138, 1);
fill: rgba(193, 76, 138, 1);
}
.block-color-red {
color: rgba(212, 76, 71, 1);
fill: rgba(212, 76, 71, 1);
}
.block-color-gray_background {
background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
background: rgba(253, 235, 236, 1);
}
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-opaquegray { background-color: rgba(255, 255, 255, 0.0375); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }

.checkbox {
display: inline-flex;
vertical-align: text-bottom;
width: 16;
height: 16;
background-size: 16px;
margin-left: 2px;
margin-right: 5px;
}

.checkbox-on {
background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
</style></head><body><article id="08cda523-e90a-4b87-8951-758e7d34ffb7" class="page sans"><header><h1 class="page-title">Create short quote videos using python</h1></header><div class="page-body"><figure id="ab7dcc08-692e-4d3e-89d8-6980a72ff5e8" class="image"><a href="https://images.unsplash.com/photo-1611162616475-46b635cb6868?ixlib=rb-1.2.1&amp;q=80&amp;cs=tinysrgb&amp;fm=jpg&amp;crop=entropy"><img src="https://images.unsplash.com/photo-1611162616475-46b635cb6868?ixlib=rb-1.2.1&amp;q=80&amp;cs=tinysrgb&amp;fm=jpg&amp;crop=entropy"/></a></figure><p id="cfc17148-57b7-4014-8874-c9464b1128ba" class="">

</p><h2 id="43826d48-88c9-48e9-be86-09a93a408282" class="">Short video generator</h2><h3 id="80031066-fe56-447e-8781-6c0ec431a53c" class=""><strong>Description</strong></h3><p id="66718c06-ce8d-42f1-bd24-ab2b2cdc597e" class="">This project creates and edits short videos using python. This application will create an awesome quote video of 15-20 sec. It will add music and quote to your video.</p><blockquote id="bf068f72-b754-4135-be4a-9b19aab908d4" class=""><em>If you can automate things then why do repetitive work</em></blockquote><p id="3d2e276f-20e6-4ad1-bf79-f5d1ae5daa8c" class="">I was watching some short videos on Youtube and suddenly got the idea of creating short videos using python automation. Instantly I opened my laptop headed to the browser and started my research. It took me a week to complete this project from research to code to deployment.</p><hr id="684ef1b5-b2a1-412e-8086-c7c73b0df418"/><h3 id="ffc2fec7-a6c8-4f30-8329-01bf8c2ab838" class=""><strong>Technologies I used</strong></h3><ul id="3bd5bec4-32de-465f-a19e-b6f3abc67ca5" class="bulleted-list"><li style="list-style-type:disc">I used python as a programming language.</li></ul><ul id="7acf5d26-b8a5-4c54-8b55-ec4a0c757481" class="bulleted-list"><li style="list-style-type:disc">For editing videos, I used moviepy python package.</li></ul><ul id="c1850a30-90ab-4d15-a43a-2d626a24f331" class="bulleted-list"><li style="list-style-type:disc">Used random quote generator API, check <a href="https://github.com/lukePeavey/quotable">here</a>.</li></ul><ul id="f5dfbf4d-4d65-4928-a256-d10ece5acc07" class="bulleted-list"><li style="list-style-type:disc">Videos from pexels, other sources. Note: Resolution size must be 1080 * 1920.</li></ul><ul id="d4571396-a307-4a14-b075-f5d666fb5f70" class="bulleted-list"><li style="list-style-type:disc">Copyright Free audio.</li></ul><hr id="b0fe6b8b-a4bd-48a8-8c16-c9166f405ea6"/><h3 id="2e8f52bb-a340-40e1-938f-6dfb7694a5b1" class="">Requirements</h3><ul id="fe66fa9f-8c16-44e3-b800-18a49655ef93" class="bulleted-list"><li style="list-style-type:disc">Python3. Download from <a href="https://www.python.org/downloads/">here</a></li></ul><ul id="a7581ccd-9591-4ac2-b616-55ce48d4b0fd" class="bulleted-list"><li style="list-style-type:disc"> moviepy package. Get it from <a href="https://pypi.org/project/moviepy/">here</a></li></ul><ul id="c40ea088-f555-470f-9de4-fec979f74032" class="bulleted-list"><li style="list-style-type:disc">ImageMagick application needs to be installed. Get it from <a href="https://www.imagemagick.org/script/download.php">here</a></li></ul><ul id="de17bdc1-fcbf-4bbf-ab92-2f688cf471a5" class="bulleted-list"><li style="list-style-type:disc">video file with resolution 1080 x 1920. get it from <a href="https://www.pexels.com/videos/">here</a></li></ul><ul id="5446188c-e8e0-42ef-b0f6-361dc5028805" class="bulleted-list"><li style="list-style-type:disc">music file</li></ul><hr id="20be7d17-41dc-4cb0-9e22-03ed61627c55"/><h3 id="7ca9fb4f-74aa-41b9-bf3b-7167245249e8" class="">How to Install and Run</h3><p id="1e8a9b66-9ea1-4f6a-8e07-fb6686e4ce8e" class="">First Let’s Create a virtual environment using cmd and switch to the created virtual environment.</p><pre id="d6cac91a-3968-4fa2-a0ef-15dc6efc4607" class="code"><code>$ python -m venv venv
$ venv/Scripts/activate.bat</code></pre><p id="612fd79e-ff83-405c-969e-7fc1fa0c0356" class="">Install the packages using the below command</p><pre id="c60ed679-96ac-45b6-b198-5c99c86cacfa" class="code"><code>$ pip install -r requirement.txt</code></pre><p id="a04d6293-7c86-4e67-aec0-ab3d4eddb5b9" class="">If you are using windows perform the below step. <strong>Mac users ignore this step. </strong>Go to path <strong>venv\Lib\site-packages\moviepy </strong>and edit the file config_defaults.py and update the IMAGEMAGICK_BINARY variable with the below path. for more details follow the <a href="https://www.imagemagick.org/script/download.php">doc</a>.</p><pre id="913f87c2-078a-42f3-ad59-62f825e84924" class="code"><code>IMAGEMAGICK_BINARY = fr&quot;C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe&quot;</code></pre><p id="5cc8163b-51f6-4974-91a3-2b510a055108" class="">Download the video from <a href="https://www.pexels.com/videos/">pexels.com</a> and place it in the root folder.</p><p id="816722dc-4c52-4881-a7bb-c9b1e52c2347" class="">Add a music file to the audio folder. It&#x27;s optional as I already added a music file for you.</p><p id="69ecbb71-eacd-43da-91c5-04361802226a" class="">Open the CMD/BASH on the root directory and run the below command</p><pre id="b9a71563-fcd3-41cb-9379-b718f2b31914" class="code"><code>$ python app.py</code></pre><p id="721339ea-970a-4c00-8eee-51dfd57ddd0c" class="">After execution, a newly edited quote video file will be generated in the root directory.</p><hr id="c110f8f8-f7f2-4162-802d-70bebf83653c"/><h3 id="d92a985f-e560-41b9-a9ad-325d32ddc9d4" class="">Credits</h3><p id="a4d1f1ef-8880-4e05-b1cb-904e0decf2dd" class=""><a href="https://www.pexels.com/">Pexels</a>:  The best free stock photos, royalty free images &amp; videos shared by creators.</p><p id="2dcbceda-a2c8-4144-be72-4f85cc6d7a25" class=""><a href="https://studio.youtube.com/channel/UCdfiJBlqq-lyE5IxwDoqYCQ/music">Youtube audio library</a>: Copyright-free music.</p><p id="49657657-330c-4bca-a4ab-61dbe7bd322f" class=""><a href="https://github.com/lukePeavey/quotable">quotable</a>: Free public quotable api.</p><hr id="33f51357-3eb3-401e-a8a5-68187bfd3757"/>
<p align="left">
<h3 id="d92a985f-e560-41b9-a9ad-325d32ddc9d4" class="">Connect with me</h3>
    <a href="https://twitter.com/ashishjaiswar_">
        <img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"/>
    </a>
    <a href="https://www.linkedin.com/in/ashish-jaiswar-developer/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
    </a>
    <a href="mailto:ashish.jaiswar687@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail"/>
    </a>
    <a href="https://medium.com/@ashishjaiswar777">
        <img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white" alt="Medium"/>
    </a>
    <a href="https://github.com/AshishJaiswar">
        <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="Github"/>
    </a>
</p><hr><p id="bd1f3151-ef45-4a2b-a05d-dbeaedbf0b2b" class=""><strong>Enjoy Coding</strong> ❤</p><p id="157ca870-5f5b-4fc4-abbd-7e8b75424d89" class="">
</p></div></article></body></html>
