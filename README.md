<!DOCTYPE html>
<!-- saved from url=(0042)https://pandao.github.io/editor.md/en.html -->
<html lang="en" class=" js flexbox flexboxlegacy canvas canvastext webgl no-touch geolocation postmessage websqldatabase indexeddb hashchange history draganddrop websockets rgba hsla multiplebgs backgroundsize borderimage borderradius boxshadow textshadow opacity cssanimations csscolumns cssgradients cssreflections csstransforms csstransforms3d csstransitions fontface generatedcontent video audio localstorage sessionstorage webworkers no-applicationcache svg inlinesvg smil svgclippaths"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta http-equiv="Cache-Control" content="no-siteapp">
		<meta name="renderer" content="webkit">
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
        <meta name="keywords" content="Editor.md,editor,Markdown Editor,Markdown,编辑器,Markdown编辑器,Markdown在线编辑器,在线编辑器,开源编辑器,开源Markdown编辑器">
        <meta name="description" content="Editor.md: a simple online markdown editor. 开源在线 Markdown 编辑器">
	    <meta name="author" content="pandao, pandao@vip.qq.com">
        <title>Editor.md - Open source online Markdown editor.</title>
        <link rel="shortcut icon" href="https://pandao.github.io/editor.md/favicon.ico" type="image/x-icon">
        <link rel="stylesheet" type="text/css" href="./README_files/planeui.min.css">
        <link rel="stylesheet" href="./README_files/editormd.min.css">
        <link rel="stylesheet" type="text/css" href="./README_files/index.css">
    <link type="text/css" rel="stylesheet" href="./README_files/codemirror.min.css"><link type="text/css" rel="stylesheet" href="./README_files/dialog.css"><link type="text/css" rel="stylesheet" href="./README_files/matchesonscrollbar.css"><link type="text/css" rel="stylesheet" href="./README_files/foldgutter.css"><script id="-lib-codemirror-codemirror-min" type="text/javascript" src="./README_files/codemirror.min.js.download"></script><script id="-lib-codemirror-modes-min" type="text/javascript" src="./README_files/modes.min.js.download"></script><script id="-lib-codemirror-addons-min" type="text/javascript" src="./README_files/addons.min.js.download"></script><script id="-lib-marked-min" type="text/javascript" src="./README_files/marked.min.js.download"></script><script id="-lib-prettify-min" type="text/javascript" src="./README_files/prettify.min.js.download"></script><script id="-lib-raphael-min" type="text/javascript" src="./README_files/raphael.min.js.download"></script><script id="-lib-underscore-min" type="text/javascript" src="./README_files/underscore.min.js.download"></script><script id="-lib-flowchart-min" type="text/javascript" src="./README_files/flowchart.min.js.download"></script><script id="-lib-jquery-flowchart-min" type="text/javascript" src="./README_files/jquery.flowchart.min.js.download"></script><script id="-lib-sequence-diagram-min" type="text/javascript" src="./README_files/sequence-diagram.min.js.download"></script><link type="text/css" rel="stylesheet" href="./README_files/katex.min.css"><script id="-cdnjs-cloudflare-com-ajax-libs-KaTeX-0-3-0-katex-min" type="text/javascript" src="./README_files/katex.min.js.download"></script></head>
    <body data-new-gr-c-s-check-loaded="14.998.0" data-gr-ext-installed="" data-new-gr-c-s-loaded="14.998.0">
        <a name="top"></a>
        <a href="https://pandao.github.io/editor.md/en.html#top" class="fa fa-arrow-circle-up fa-3x pui-text-blue-400" id="go-to-top" style="display: none;"></a>
        <div class="pui-layout">
            <header class="pui-bg-blue page-header">
                <div class="pui-layout pui-layout-fixed pui-layout-fixed-1200 pui-layout-fixed-1360">
                    <h1 class="pui-text-center pui-text-xxxxxl page-title animated zoomInDown">
                        <a href="https://pandao.github.io/editor.md/index.html" class="pui-text-white">
                            <i class="editormd-logo editormd-logo-2x"></i><strong>Editor.md</strong>
                        </a>
                    </h1>
                    <p class="pui-text-center pui-text-xl animated zoomInDown">Open source online Markdown editor.</p>
                    <menu class="pui-text-center page-menu animated zoomInDown">
                        <ul class="pui-menu pui-menu-inline pui-menu-radius">
                            <li>
                                <a href="https://pandao.github.io/editor.md/en.html#download"><i class="fa fa-cloud-download"></i> Download</a>
                            </li>
                            <li>
                                <a href="http://editor.md.ipandao.com/examples/index.html"><i class="fa fa-flask"></i> Examples <i class="pui-arrow-down"></i></a>
                                <ul class="pui-menu pui-menu-dropdown pui-z-depth-2">
                                    <li>
                                        <a href="http://editor.md.ipandao.com/examples/simple.html">Simple example</a>
                                    </li>
                                    <li>
                                        <a href="http://editor.md.ipandao.com/examples/full.html">Full example</a>
                                    </li>
                                    <li>
                                        <a href="http://editor.md.ipandao.com/examples/html-preview-markdown-to-html.html">Markdown To HTML</a>
                                    </li>
                                    <li>
                                        <a href="http://editor.md.ipandao.com/examples/form-get-value.html">Get value on Form</a>
                                    </li>
                                    <li class="has-submenu">
                                        <a href="javascript:;">Markdown Extras</a>
                                        <ul class="pui-menu pui-menu-dropdown pui-z-depth-2">
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/toc.html">ToC (Table of Contents)</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/task-lists.html">GFM task lists</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/emoji.html">Emoji</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/@links.html">@Links</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/katex.html">TeX (KaTeX)</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/flowchart.html">FlowChart</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/sequence-diagram.html">Sequence diagram</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/html-tags-decode.html">HTML tags decode</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="has-submenu">
                                        <a href="javascript:;">Custom Editor.md</a>
                                        <ul class="pui-menu pui-menu-dropdown pui-z-depth-2">
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/define-plugin.html">Define plugin</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/themes.html">Custom editor theme</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/custom-toolbar.html">Custom toolbar</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/custom-keyboard-shortcuts.html">Custom keyboard shortcuts</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/change-mode.html">Change mode</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/manually-load-modules.html">Manually load modules</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/multi-editormd.html">Multi Editor.md</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/readonly.html">Read only mode</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/code-fold.html">Code fold</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/sync-scrolling.html">Bisync / Single sync scrolling</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/external-use.html">External using method</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/multi-languages.html">Multi-languages</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/auto-height.html">Auto height</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/dynamic-create-editormd.html">Dynamic create Editor.md</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/search-replace.html">Search / Replace</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/set-get-replace-selection.html">Insert value, Set/Get/Replace selection text</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="has-submenu">
                                        <a href="javascript:;">Event handle</a>
                                        <ul class="pui-menu pui-menu-dropdown pui-z-depth-2">
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/on-off.html">On / Off (bind/unbind)</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/onload.html">Onload</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/onchange.html">Onchange</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/onresize.html">Onresize</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/onfullscreen.html">Onfullscreen / OnfullscreenExit</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/onpreviewing-onpreviewed.html">Onpreviewing / Onpreviewed</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/onwatch-onunwatch.html">Onwatch / Onunwatch</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/onscroll-onpreviewscroll.html">Onscroll / Onpreviewscroll</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="has-submenu">
                                        <a href="javascript:;">Image upload</a>
                                        <ul class="pui-menu pui-menu-dropdown pui-z-depth-2">
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/image-upload.html">Same domain upload</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/image-cross-domain-upload.html">Cross-domain upload</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="has-submenu">
                                        <a href="javascript:;">Using Require.js, Sea.js, Zepto.js</a>
                                        <ul class="pui-menu pui-menu-dropdown pui-z-depth-2">
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/use-requirejs.html">Using Require.js</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/use-seajs.html">Using Sea.js</a>
                                            </li>
                                            <li>
                                                <a href="http://editor.md.ipandao.com/examples/use-zepto.html">Using Zepto.js</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li>
                                        <a href="http://editor.md.ipandao.com/examples/index.html">More...</a>
                                    </li>
                                </ul>
                            </li>
                            <li>
                                <a href="https://pandao.github.io/editor.md/en.html#dependents"><i class="fa fa-gears"></i> Dependents</a>
                            </li>
                            <li>
                                <a href="https://pandao.github.io/editor.md/en.html#license"><i class="fa fa-check"></i> License</a>
                            </li>
                            <li>
                                <a href="https://github.com/pandao/editor.md/blob/master/CHANGE.md" target="_blank"><i class="fa fa-refresh"></i> Changes</a>
                            </li>
                            <li>
                                <a href="https://github.com/pandao/editor.md/issues" target="_blank"><i class="fa fa-question-circle"></i> Issues</a>
                            </li>
                            <li>
                                <a href="https://github.com/pandao/editor.md" target="_blank"><i class="fa fa-github"></i> Github</a>
                            </li>
                            <li>
                                <a href="https://gitee.com/pandao/editor.md" target="_blank"><i class="fa fa-git"></i> Git@OSC</a>
                            </li>
                            <li>
                                <a href="https://pandao.github.io/editor.md/index.html"><i class="fa fa-language"></i> 中文版</a>
                            </li>
                        </ul>
                    </menu>   
                    <div class="page-header-container">
                        <div class="editormd pui-z-depth-3 pui-bg-white editormd-vertical" id="index-editormd" style="width: 100%; height: 580px;"><textarea class="editormd-markdown-textarea" placeholder="Enjoy Markdown! coding now..." name="index-editormd-markdown-doc" style="display: none;"># Solving the B&amp;W sheeps problem

The goal of this code is to move all the black sheeps to the right and all the white sheeps to the left knowing that :
- A sheep must move to an empty space, or jump over another sheep and land on an empty space
- A sheep can't jump over more than one sheep
- A sheep always faces the same direction and can't move backward or jump backward

Let's represent the white and black sheeps in a list like the following example,
['B', 'B', 'B', 'B', 'B', 'space', 'W', 'W', 'W', 'W', 'W']

The index of the empty  is the key of all the moves :

If the empty space is between two sheeps of the same color, we jump with the sheep with the other  color to the desired direction.

If the empty space is between two sheeps with different colors, we move forward the sheep that makes the empty space between two sheeps with the same color.





system info:

- ubuntu 18.04

- python 3.6.9





## usage


```bash
$ python XQUANT.py  --b number of black sheeps desired   --w number of white sheeps desired
```</textarea><div class="CodeMirror cm-s-default CodeMirror-wrap CodeMirror-focused" style="font-size: 13px; width: 601px; margin-top: 81px; height: 500px;"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 288px; left: 64.1094px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-vscrollbar" cm-not-content="true" style="bottom: 0px; display: block;"><div style="min-width: 1px; height: 1000px;"></div></div><div class="CodeMirror-hscrollbar" cm-not-content="true"><div style="height: 100%; min-height: 1px; width: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 48px; margin-bottom: -7px; border-right-width: 23px; min-height: 997px; padding-right: 7px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines"><div style="position: relative; outline: none;"><div class="CodeMirror-measure"><pre>x</pre><div class="CodeMirror-linenumber CodeMirror-gutter-elt"><div>1</div></div><div class="CodeMirror-linenumber CodeMirror-gutter-elt"><div>22</div></div></div><div class="CodeMirror-measure"><pre><span style="padding-right: 0.1px;"><span class="cm-header cm-header-3">###End</span></span></pre></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors" style=""><div class="CodeMirror-cursor" style="left: 16.1094px; top: 414px; height: 22px;">&nbsp;</div></div><div class="CodeMirror-code" style=""><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">1</div><div class="CodeMirror-gutter-elt" style="left: 38px; width: 9px;"><div class="CodeMirror-foldgutter-open CodeMirror-guttermarker-subtle"></div></div></div><pre class=""><span style="padding-right: 0.1px;"><span class="cm-header cm-header-1"># Solving the B&amp;W sheeps problem</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">2</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">3</div></div><pre class=""><span style="padding-right: 0.1px;">The goal of this code is to move all the black sheeps to the right and all the white sheeps to the left knowing that :</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">4</div></div><pre class=""><span style="padding-right: 0.1px;">- A sheep must move to an empty space, or jump over another sheep and land on an empty space</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">5</div></div><pre class=""><span style="padding-right: 0.1px;">- A sheep can't jump over more than one sheep</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">6</div></div><pre class=""><span style="padding-right: 0.1px;">- A sheep always faces the same direction and can't move backward or jump backward</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">7</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">8</div></div><pre class=""><span style="padding-right: 0.1px;">Let's represent the white and black sheeps in a list like the following example,</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">9</div></div><pre class=""><span style="padding-right: 0.1px;">['B', 'B', 'B', 'B', 'B', 'space', 'W', 'W', 'W', 'W', 'W']</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">10</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">11</div></div><pre class=""><span style="padding-right: 0.1px;">The index of the empty  is the key of all the moves :</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">12</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">13</div></div><pre class=""><span style="padding-right: 0.1px;"><span class="cm-cm-overlay cm-matchhighlight">If</span> the empty space is between two sheeps of the same color, we jump with the sheep with the other  color to the desired direction.</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">14</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div class="CodeMirror-activeline" style="position: relative;"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">15</div></div><pre class=""><span style="padding-right: 0.1px;"><span class="cm-cm-overlay cm-matchhighlight">If</span> the empty space is between two sheeps with different colors, we move forward the sheep that makes the empty space between two sheeps with the same color.</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">16</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">17</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">18</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">19</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">20</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">21</div></div><pre class=""><span style="padding-right: 0.1px;">system info:</span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">22</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">23</div></div><pre class=""><span style="padding-right: 0.1px;"><span class="cm-variable-2">- ubuntu 18.04</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">24</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">25</div></div><pre class=""><span style="padding-right: 0.1px;"><span class="cm-variable-2">- python 3.6.9</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">26</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">27</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">28</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">29</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">30</div></div><pre class=""><span style="padding-right: 0.1px;"><span cm-text="">​</span></span></pre></div><div style="position: relative;"><div class="CodeMirror-gutter-wrapper" style="left: -48px; width: 48px;"><div class="CodeMirror-linenumber CodeMirror-gutter-elt" style="left: 0px; width: 20px;">31</div><div class="CodeMirror-gutter-elt" style="left: 38px; width: 9px;"><div class="CodeMirror-foldgutter-open CodeMirror-guttermarker-subtle"></div></div></div><pre class=""><span style="padding-right: 0.1px;"><span class="cm-header cm-header-2">## usage</span></span></pre></div></div></div></div></div></div><div style="position: absolute; height: 23px; width: 1px; top: 997px;"></div><div class="CodeMirror-gutters" style="height: 1020px;"><div class="CodeMirror-gutter CodeMirror-linenumbers" style="width: 28px;"></div><div class="CodeMirror-gutter CodeMirror-foldgutter"></div></div></div></div><a href="javascript:;" class="fa fa-close editormd-preview-close-btn"></a>

<div class="editormd-preview" style="display: block; width: 600px; top: 81px; height: 500px;"><div class="markdown-body editormd-preview-container" previewcontainer="true" style="padding: 20px;"><h1 id="h1-solving-the-b-amp-w-sheeps-problem"><a name="Solving the B&amp;W sheeps problem" class="reference-link"></a><span class="header-link octicon octicon-link"></span>Solving the B&amp;W sheeps problem</h1><p>The goal of this code is to move all the black sheeps to the right and all the white sheeps to the left knowing that :</p>
<ul>
<li>A sheep must move to an empty space, or jump over another sheep and land on an empty space</li><li>A sheep can’t jump over more than one sheep</li><li>A sheep always faces the same direction and can’t move backward or jump backward</li></ul>
<p>Let’s represent the white and black sheeps in a list like the following example,<br>[‘B’, ‘B’, ‘B’, ‘B’, ‘B’, ‘space’, ‘W’, ‘W’, ‘W’, ‘W’, ‘W’]</p>
<p>The index of the empty  is the key of all the moves :</p>
<p>If the empty space is between two sheeps of the same color, we jump with the sheep with the other  color to the desired direction.</p>
<p>If the empty space is between two sheeps with different colors, we move forward the sheep that makes the empty space between two sheeps with the same color.</p>
<p>system info:</p>
<ul>
<li><p>ubuntu 18.04</p>
</li><li><p>python 3.6.9</p>
</li></ul>
<h2 id="h2-usage"><a name="usage" class="reference-link"></a><span class="header-link octicon octicon-link"></span>usage</h2><pre class="prettyprint linenums prettyprinted" style=""><ol class="linenums"><li class="L0"><code class="lang-bash"><span class="pln">$ python XQUANT</span><span class="pun">.</span><span class="pln">py  </span><span class="pun">--</span><span class="pln">b number of black sheeps desired   </span><span class="pun">--</span><span class="pln">w number of white sheeps desired</span></code></li></ol></pre>
</div></div>
<div class="editormd-container-mask" style="display: none;"></div>
<div class="editormd-mask"></div><div class="editormd-toolbar" style="display: block; position: absolute; width: 100%; left: 0px;"><div class="editormd-toolbar-container"><ul class="editormd-menu"><li><a href="javascript:;" title="Undo(Ctrl+Z)" unselectable="on"><i class="fa fa-undo" name="undo" unselectable="on"></i></a></li><li><a href="javascript:;" title="Redo(Ctrl+Y)" unselectable="on"><i class="fa fa-repeat" name="redo" unselectable="on"></i></a></li><li class="divider" unselectable="on">|</li><li><a href="javascript:;" title="Bold" unselectable="on"><i class="fa fa-bold" name="bold" unselectable="on"></i></a></li><li><a href="javascript:;" title="Strikethrough" unselectable="on"><i class="fa fa-strikethrough" name="del" unselectable="on"></i></a></li><li><a href="javascript:;" title="Italic" unselectable="on"><i class="fa fa-italic" name="italic" unselectable="on"></i></a></li><li><a href="javascript:;" title="Block quote" unselectable="on"><i class="fa fa-quote-left" name="quote" unselectable="on"></i></a></li><li><a href="javascript:;" title="Words first letter convert to uppercase" unselectable="on"><i class="fa" name="ucwords" style="font-size:20px;margin-top: -3px;">Aa</i></a></li><li><a href="javascript:;" title="Selection text convert to uppercase" unselectable="on"><i class="fa fa-font" name="uppercase" unselectable="on"></i></a></li><li><a href="javascript:;" title="Selection text convert to lowercase" unselectable="on"><i class="fa" name="lowercase" style="font-size:24px;margin-top: -10px;">a</i></a></li><li class="divider" unselectable="on">|</li><li><a href="javascript:;" title="Heading 1" unselectable="on"><i class="fa editormd-bold" name="h1" unselectable="on">H1</i></a></li><li><a href="javascript:;" title="Heading 2" unselectable="on"><i class="fa editormd-bold" name="h2" unselectable="on">H2</i></a></li><li><a href="javascript:;" title="Heading 3" unselectable="on"><i class="fa editormd-bold" name="h3" unselectable="on">H3</i></a></li><li><a href="javascript:;" title="Heading 4" unselectable="on"><i class="fa editormd-bold" name="h4" unselectable="on">H4</i></a></li><li><a href="javascript:;" title="Heading 5" unselectable="on"><i class="fa editormd-bold" name="h5" unselectable="on">H5</i></a></li><li><a href="javascript:;" title="Heading 6" unselectable="on"><i class="fa editormd-bold" name="h6" unselectable="on">H6</i></a></li><li class="divider" unselectable="on">|</li><li><a href="javascript:;" title="Unordered list" unselectable="on"><i class="fa fa-list-ul" name="list-ul" unselectable="on"></i></a></li><li><a href="javascript:;" title="Ordered list" unselectable="on"><i class="fa fa-list-ol" name="list-ol" unselectable="on"></i></a></li><li><a href="javascript:;" title="Horizontal rule" unselectable="on"><i class="fa fa-minus" name="hr" unselectable="on"></i></a></li><li class="divider" unselectable="on">|</li><li><a href="javascript:;" title="Link" unselectable="on"><i class="fa fa-link" name="link" unselectable="on"></i></a></li><li><a href="javascript:;" title="Reference link" unselectable="on"><i class="fa fa-anchor" name="reference-link" unselectable="on"></i></a></li><li><a href="javascript:;" title="Image" unselectable="on"><i class="fa fa-picture-o" name="image" unselectable="on"></i></a></li><li><a href="javascript:;" title="Code inline" unselectable="on"><i class="fa fa-code" name="code" unselectable="on"></i></a></li><li><a href="javascript:;" title="Preformatted text / Code block (Tab indent)" unselectable="on"><i class="fa fa-file-code-o" name="preformatted-text" unselectable="on"></i></a></li><li><a href="javascript:;" title="Code block (Multi-languages)" unselectable="on"><i class="fa fa-file-code-o" name="code-block" unselectable="on"></i></a></li><li><a href="javascript:;" title="Tables" unselectable="on"><i class="fa fa-table" name="table" unselectable="on"></i></a></li><li><a href="javascript:;" title="Datetime" unselectable="on"><i class="fa fa-clock-o" name="datetime" unselectable="on"></i></a></li><li><a href="javascript:;" title="Emoji" unselectable="on"><i class="fa fa-smile-o" name="emoji" unselectable="on"></i></a></li><li><a href="javascript:;" title="HTML Entities" unselectable="on"><i class="fa fa-copyright" name="html-entities" unselectable="on"></i></a></li><li><a href="javascript:;" title="Page break" unselectable="on"><i class="fa fa-newspaper-o" name="pagebreak" unselectable="on"></i></a></li><li class="divider" unselectable="on">|</li><li><a href="javascript:;" title="" unselectable="on"><i class="fa fa-terminal" name="goto-line" unselectable="on"></i></a></li><li><a href="javascript:;" title="Unwatch" unselectable="on"><i class="fa fa-eye-slash" name="watch" unselectable="on"></i></a></li><li><a href="javascript:;" title="HTML Preview (Press Shift + ESC exit)" unselectable="on"><i class="fa fa-desktop" name="preview" unselectable="on"></i></a></li><li><a href="javascript:;" title="Fullscreen (Press ESC exit)" unselectable="on"><i class="fa fa-arrows-alt" name="fullscreen" unselectable="on"></i></a></li><li><a href="javascript:;" title="Clear" unselectable="on"><i class="fa fa-eraser" name="clear" unselectable="on"></i></a></li><li><a href="javascript:;" title="Search" unselectable="on"><i class="fa fa-search" name="search" unselectable="on"></i></a></li><li class="divider" unselectable="on">|</li><li><a href="javascript:;" title="Help" unselectable="on"><i class="fa fa-question-circle" name="help" unselectable="on"></i></a></li><li><a href="javascript:;" title="About Editor.md" unselectable="on"><i class="fa fa-info-circle" name="info" unselectable="on"></i></a></li></ul></div></div></div>                        
                    </div>
                </div>
            </header>
            <div class="pui-grid pui-layout pui-layout-fixed pui-layout-fixed-1200 page-content">
                <div class="pui-row">
                    <div class="pui-grid-xs-8">
                        <a name="start"></a>
                        <div class="pui-card pui-card-simple">
                            <div class="pui-card-title">
                                <h1 class="pui-text-left">Example</h1>
                            </div>
                            <div class="pui-card-box">
                                <div class="code-box">
                                    <pre class="prettyprint lang-html example-code prettyprinted" style=""><span class="tag">&lt;link</span><span class="pln"> </span><span class="atn">rel</span><span class="pun">=</span><span class="atv">"stylesheet"</span><span class="pln"> </span><span class="atn">href</span><span class="pun">=</span><span class="atv">"editormd/css/editormd.css"</span><span class="pln"> </span><span class="tag">/&gt;</span><span class="pln">
</span><span class="tag">&lt;div</span><span class="pln"> </span><span class="atn">id</span><span class="pun">=</span><span class="atv">"test-editor"</span><span class="tag">&gt;</span><span class="pln">
    </span><span class="tag">&lt;textarea</span><span class="pln"> </span><span class="atn">style</span><span class="pun">=</span><span class="atv">"</span><span class="pln">display</span><span class="pun">:</span><span class="pln">none</span><span class="pun">;</span><span class="atv">"</span><span class="tag">&gt;</span><span class="pln">### Editor.md

**Editor.md**: The open source embeddable online markdown editor, based on CodeMirror &amp; jQuery &amp; Marked.
    </span><span class="tag">&lt;/textarea&gt;</span><span class="pln">
</span><span class="tag">&lt;/div&gt;</span><span class="pln">
</span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js"</span><span class="tag">&gt;&lt;/script&gt;</span><span class="pln">
</span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">src</span><span class="pun">=</span><span class="atv">"editormd/editormd.min.js"</span><span class="tag">&gt;&lt;/script&gt;</span><span class="pln">
</span><span class="tag">&lt;script</span><span class="pln"> </span><span class="atn">type</span><span class="pun">=</span><span class="atv">"text/javascript"</span><span class="tag">&gt;</span><span class="pln">
    $</span><span class="pun">(</span><span class="kwd">function</span><span class="pun">()</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
        </span><span class="kwd">var</span><span class="pln"> editor </span><span class="pun">=</span><span class="pln"> editormd</span><span class="pun">(</span><span class="str">"test-editor"</span><span class="pun">,</span><span class="pln"> </span><span class="pun">{</span><span class="pln">
            </span><span class="com">// width  : "100%",</span><span class="pln">
            </span><span class="com">// height : "100%",</span><span class="pln">
            path   </span><span class="pun">:</span><span class="pln"> </span><span class="str">"editormd/lib/"</span><span class="pln">
        </span><span class="pun">});</span><span class="pln">
    </span><span class="pun">});</span><span class="pln">
</span><span class="tag">&lt;/script&gt;</span></pre>
                                    <span class="copy-btn" data-clipboard-text="&lt;link rel=&quot;stylesheet&quot; href=&quot;editormd/css/editormd.css&quot; /&gt;
&lt;div id=&quot;test-editor&quot;&gt;
    &lt;textarea style=&quot;display:none;&quot;&gt;### Editor.md

**Editor.md**: The open source embeddable online markdown editor, based on CodeMirror &amp; jQuery &amp; Marked.
    &lt;/textarea&gt;
&lt;/div&gt;
&lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/jquery/1.11.3/jquery.min.js&quot;&gt;&lt;/script&gt;
&lt;script src=&quot;editormd/editormd.min.js&quot;&gt;&lt;/script&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
    $(function() {
        var editor = editormd(&quot;test-editor&quot;, {
            // width  : &quot;100%&quot;,
            // height : &quot;100%&quot;,
            path   : &quot;editormd/lib/&quot;
        });
    });
&lt;/script&gt;">Copy</span>
                                </div>
                                <p class="pui-text-right"><a href="http://editor.md.ipandao.com/examples/" class="link pui-text-blue">More Examples &gt;&gt;</a></p>
                            </div>
                        </div>
                    </div>
                    <div class="pui-grid-xs-4">
                        <div class="pui-card-title">
                            <h1 class="pui-text-left">Features</h1>
                        </div>
                        <div class="pui-card-box">
                            <ul>
                                <li>Support Standard Markdown / CommonMark and GFM(GitHub Flavored Markdown);</li>
                                <li>Full-featured: Real-time Preview, <a href="http://editor.md.ipandao.com/examples/image-upload.html" class="link pui-text-blue">Image (cross-domain) upload</a>, Preformatted text/Code blocks/Tables insert, Code fold, Search replace, Read only, Themes, Multi-languages, L18n, HTML entities, Code syntax highlighting...;</li>
                                <li>Markdown Extras : Support <a href="http://editor.md.ipandao.com/examples/toc.html" class="link pui-text-blue">ToC (Table of Contents)</a>, <a href="http://editor.md.ipandao.com/examples/emoji.html" class="link pui-text-blue">Emoji</a>, <a href="http://editor.md.ipandao.com/examples/task-lists.html" class="link pui-text-blue">Task lists</a>, <a href="http://editor.md.ipandao.com/examples/@links.html" class="link pui-text-blue">@Links</a>...;</li>
                                <li>Support <a href="http://editor.md.ipandao.com/examples/katex.html" class="link pui-text-blue">TeX (LaTeX expressions, Based on KaTeX)</a>, <a href="http://editor.md.ipandao.com/examples/flowchart.html" class="link pui-text-blue">Flowchart</a> and <a href="http://editor.md.ipandao.com/examples/sequence-diagram.html" class="link pui-text-blue">Sequence Diagram</a> of Markdown extended syntax;</li>
                                <li>Support identification, interpretation, fliter of the HTML tags;</li>
                                <li>Support AMD/CMD (Require.js &amp; Sea.js) Module Loader, and Custom/define editor plugins;</li>
                                <li>Compatible with all major browsers (IE8+), compatible Zepto.js and iPad;</li>
                                <li>Support Custom theme styles;</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            <hr class="pui-hr pui-layout-fixed pui-layout-fixed-1200">
            <div class="pui-grid pui-layout pui-layout-fixed pui-layout-fixed-1200 page-content">
                <div class="pui-row">
                    <div class="pui-grid-xs-12 pui-grid-sm-4 pui-grid-md-4">
                        <a name="download"></a>
                        <div class="pui-card pui-card-simple">
                            <div class="pui-card-title">
                                <h1>Download &amp; install</h1>
                            </div>
                            <div class="pui-card-box">
                                <p>Latest version: v1.5.0，Update: 2015-06-09</p>
                                <p><a href="https://github.com/pandao/editor.md/archive/master.zip" class="pui-btn pui-btn-secondary"><i class="fa fa-lg fa-github"></i> Github download</a></p>
                                <br>
                                <p><img src="./README_files/editor.md.svg"> <img src="./README_files/editor.md(1).svg"></p>
                                <br>
                                <p>Or NPM install:</p>
                                <p><code>npm install editor.md</code></p>
                                <p><img src="./README_files/editor.md(2).svg"></p>
                                <p>Or Bower install: </p>
                                <p><code>bower install editor.md</code></p>
                                <p><img src="./README_files/editor.md(3).svg"></p>
                                <br>
                                <p><strong class="pui-text-md">Change logs: </strong></p>
                                <p><a href="https://github.com/pandao/editor.md/blob/master/CHANGE.md" class="pui-link" target="_blank">CHANGES</a></p>
                            </div>
                        </div>
                    </div>
                    <div class="pui-grid-xs-12 pui-grid-sm-4 pui-grid-md-4">                        
                        <a name="dependents"></a>
                        <div class="pui-card pui-card-simple">
                            <div class="pui-card-title">
                                <h1>Dependents</h1>
                            </div>
                            <div class="pui-card-box">
                                <p>Projects :</p>
                                <ul>
                                    <li>
                                        <a href="http://codemirror.net/" title="CodeMirror" target="_blank">CodeMirror</a>
                                    </li>
                                    <li>
                                        <a href="https://github.com/chjj/marked" title="marked" target="_blank">marked</a>
                                    </li>
                                    <li>
                                        <a href="http://jquery.com/" title="jQuery" target="_blank">jQuery</a>
                                    </li>
                                    <li>
                                        <a href="http://fontawesome.io/" title="FontAwesome" target="_blank">FontAwesome</a>
                                    </li>
                                    <li>
                                        <a href="https://github.com/sindresorhus/github-markdown-css" title="github-markdown.css" target="_blank">github-markdown.css</a>
                                    </li>
                                    <li>
                                        <a href="http://khan.github.io/KaTeX/" title="KaTeX" target="_blank">KaTeX</a>
                                    </li>
                                    <li>
                                        <a href="http://raphaeljs.com/" title="Rephael.js" target="_blank">Rephael.js</a>
                                    </li>
                                    <li>
                                        <a href="http://code.google.com/p/google-code-prettify/" title="prettify.js" target="_blank">prettify.js</a>
                                    </li>
                                    <li>
                                        <a href="http://adrai.github.io/flowchart.js/" title="flowchart.js" target="_blank">flowchart.js</a>
                                    </li>
                                    <li>
                                        <a href="http://bramp.github.io/js-sequence-diagrams/" title="sequence-diagram.js" target="_blank">sequence-diagram.js</a>
                                    </li>
                                    <li>
                                        <a href="https://github.com/pandao/prefixes.scss" title="Prefixes.scss" target="_blank">Prefixes.scss</a>
                                    </li>
                                </ul>
                                <br>
                                <p>Development tools :</p>
                                <ul>
                                    <li>
                                        <a href="https://code.visualstudio.com/" title="Visual Studio Code" target="_blank">Visual Studio Code</a>
                                    </li>
                                    <li>
                                        <a href="http://sass-lang.com/" title="Sass/Scss" target="_blank">Sass/Scss</a>
                                    </li>
                                    <li>
                                        <a href="http://gulpjs.com/" title="Gulp.js" target="_blank">Gulp.js</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="pui-grid-xs-12 pui-grid-sm-4 pui-grid-md-4">                
                        <a name="license"></a>
                        <div class="pui-card pui-card-simple">
                            <div class="pui-card-title">
                                <h1>License</h1>
                            </div>
                            <div class="pui-card-box">
                                <p>Editor.md follows the <a href="https://github.com/pandao/editor.md/blob/master/LICENSE" class="pui-link" target="_blank">MIT License</a>, Anyone can freely use.</p>
                                <br>
                                <p><a href="https://github.com/pandao/editor.md/issues/new" class="pui-btn pui-btn-secondary" target="_blank" title="Submit bugs or new issues"><i class="fa fa-lg fa-github"></i> Submit bugs or new issues</a></p>
                                <p><img src="./README_files/editor.md(4).svg"></p>
                                <div class="github-buttons">
                                    <p>Fork me on Github :</p>
                                    <p><iframe src="./README_files/github-btn.html" frameborder="0" scrolling="0" width="160px" height="30px"></iframe></p>
                                    <p><iframe src="./README_files/github-btn(1).html" frameborder="0" scrolling="0" width="160px" height="30px"></iframe></p>
                                    <p><iframe src="./README_files/github-btn(2).html" frameborder="0" scrolling="0" width="160px" height="30px"></iframe>
</p>
                                </div>
                            </div>
                        </div>                        
                    </div>
                </div>
            </div>
            <hr class="pui-hr pui-layout-fixed pui-layout-fixed-1200">
            <div class="pui-grid pui-layout pui-layout-fixed pui-layout-fixed-1200 page-content">
                <div class="pui-row">
                    <div class="pui-grid-xs-12">
                        <a name="users"></a>
                        <div class="pui-card pui-card-simple">
                            <div class="pui-card-title">
                                <h1 class="pui-text-center">Users</h1>
                            </div>
                            <div class="pui-card-box">
                                <ul class="pui-menu pui-menu-inline case-list">
                                    <li>
                                        <a href="https://www.alipay.com/" target="_blank" title="Alipay">
                                            <img src="./README_files/alipay.png" alt="Alipay">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.alibaba.com/" target="_blank" title="Alibaba">
                                            <img src="./README_files/alibaba.png" alt="Alibaba">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.huawei.com/" target="_blank" title="Huawei">
                                            <img src="./README_files/huawei.png" alt="Huawei">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://work.weixin.qq.com/" target="_blank" title="WeChat Work">
                                            <img src="./README_files/wechat-work.png" alt="WeChat Work">
                                        </a>
                                    </li>
                                </ul>
                                <ul class="pui-menu pui-menu-inline case-list">
                                    <li>
                                        <a href="https://www.jd.com/" target="_blank" title="JD.com">
                                            <img src="./README_files/jd.png" alt="JD.com">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.360.cn/" target="_blank" title="360">
                                            <img src="./README_files/360.png" alt="360">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.4399.com/" target="_blank" title="4399">
                                            <img src="./README_files/4399.png" alt="4399">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.oschina.net/" target="_blank" title="OSChina.net">
                                            <img src="./README_files/oschina.png" alt="OSChina.net">
                                        </a>
                                    </li>
                                </ul>
                                <ul class="pui-menu pui-menu-inline case-list">
                                    <li>
                                        <a href="https://www.youdao.com/" target="_blank" title="Youdao">
                                            <img src="./README_files/youdao.jpg" alt="Youdao">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.yy.com/" target="_blank" title="YY.com">
                                            <img src="./README_files/yy.jpg" alt="YY.com">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.jumei.com/" target="_blank" title="JUMEI">
                                            <img src="./README_files/jumei.jpg" alt="JUMEI">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.9you.com/" target="_blank" title="9you.com">
                                            <img src="./README_files/9you.jpg" alt="9you.com">
                                        </a>
                                    </li>
                                </ul>
                                <ul class="pui-menu pui-menu-inline case-list">
                                    <li>
                                        <a href="https://www.csdn.net/" target="_blank" title="CSDN">
                                            <img src="./README_files/csdn.jpg" alt="CSDN">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.mi.com/" target="_blank" title="Xiaomi MI.com">
                                            <img src="./README_files/xiaomi.png" alt="Xiaomi MI.com">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.meizu.com/" target="_blank" title="MEIZU">
                                            <img src="./README_files/meizu.png" alt="MEIZU">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://golangtc.com/" target="_blank" title="Golang Chinese community">
                                            <img src="./README_files/golangtc.jpg" alt="Golang Chinese community">
                                        </a>
                                    </li>
                                </ul>
                                <ul class="pui-menu pui-menu-inline case-list">
                                    <li>
                                        <a href="https://www.nio.cn/" target="_blank" title="NIO">
                                            <img src="./README_files/nio.png" alt="NIO">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="http://edn.egret.com/cn/" target="_blank" title="Egret HTML5 Game Engine">
                                            <img src="./README_files/egret-engine.jpg" alt="Egret HTML5 Game Engine">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="http://bbs.pkbigdata.com/" target="_blank" title="DataCastle">
                                            <img src="./README_files/datacastle.jpg" alt="DataCastle">
                                        </a>
                                    </li>
                                    <li>
                                        <a href="https://www.showdoc.cc/" target="_blank" title="ShowDoc：一个非常适合IT团队的在线API文档、技术文档工具">
                                            <img src="./README_files/showdoc.png" alt="ShowDoc">
                                        </a>
                                    </li>     
                                </ul>
                                <br>
                                <p class="pui-text-center"><a href="mailto:editor.md@ipandao.com" class="pui-text-blue"><i class="fa fa-envelope-o"></i> Contact Us:</a> editor.md@ipandao.com</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <hr class="pui-hr pui-layout-fixed pui-layout-fixed-1200">
            <footer class="pui-layout pui-layout-fixed pui-layout-fixed-1200 page-footer pui-clear">
                <h1 class="pui-text-lg pui-right pui-text-center">
                    <p>
                        <img src="./README_files/editormd-logo-64x64.png">
                        <span class="pui-block pui-text-gray pui-text-normal">Editor.md</span>
                    </p>
                </h1>
                <p>Copyright © 2015-2019 <a href="https://github.com/pandao/editor.md" class="pui-link" target="_blank">Editor.md</a>, <a href="https://github.com/pandao/editor.md/blob/master/LICENSE" class="pui-link" target="_blank">MIT license.</a></p>
                <p>Design &amp; Develop By: <a href="https://github.com/pandao" class="pui-link" target="_blank">Pandao</a>
                 <a href="https://github.com/pandao" target="_blank"><i class="fa fa-github fa-lg"></i></a>
                 <a href="https://twitter.com/ipandao" target="_blank"><i class="fa fa-twitter fa-lg pui-text-blue"></i></a>
                 <a href="http://weibo.com/ipandao" target="_blank"><i class="fa fa-weibo fa-lg pui-text-red"></i></a>&nbsp;&nbsp; 
                 <script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1254310986'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s11.cnzz.com/stat.php%3Fid%3D1254310986%26show%3Dpic' type='text/javascript'%3E%3C/script%3E"));</script><span id="cnzz_stat_icon_1254310986"><a href="https://www.cnzz.com/stat/website.php?web_id=1254310986" target="_blank" title="站长统计"><img border="0" hspace="0" vspace="0" src="./README_files/pic.gif"></a></span><script src="./README_files/stat.php" type="text/javascript"></script><script src="./README_files/core.php" charset="utf-8" type="text/javascript"></script>
                </p>
            </footer>
        </div>
        
        <script src="./README_files/jquery.min.js.download"></script>

        <!--[if lt IE 9]>
        <script type="text/javascript" src="https://pandao.github.io/dist/js/planeui.patch.ie8.min.js"></script>
        <![endif]-->

        <!--[if lt IE 10]>
        <script type="text/javascript" src="https://pandao.github.io/dist/js/planeui.patch.ie9.min.js"></script>
        <![endif]-->

        <script type="text/javascript" src="./README_files/planeui.js.download"></script>
        <script src="./README_files/editormd.min.js.download"></script>   
        <script src="./README_files/clipboard.min.js.download"></script>
        <script src="./README_files/en.js.download"></script>
        <script src="./README_files/index-en.js.download"></script>
    

<i title="Raphaël Colour Picker" style="display: none; color: white;"></i></body></html>