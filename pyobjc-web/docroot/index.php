<?
$title = "Home";
$cvs_author = '$Author: bbum $';
$cvs_date = '$Date: 2002/12/19 21:05:54 $';
$is_home = 1;

$metatags = '<meta name="description" content="PyObjC, a universal bridge between the Objective-C and Python languages.">
<meta name="keywords" content="Mac OS X, Darwin, GNUStep, Unix, software, distribution, Python, Objective-C, ObjC, PyObjC">
';

include "header.inc";
?>

<p>
The PyObjC project aims to provide a bridge between the Python and Objective-C programming languages.  The bridge is intended to be fully bidirectional, allowing the Objective-C programmer transparent access to Python based functionality and the Python programmer to take full advantage of the power provided by various Objective-C based toolkits.</p>
<p>
Currently, development of the bridge is primarily focused upon the <a href="http://www.apple.com/macosx/">Mac OS X</a> and <a href="http://www.opensource.apple.com/">Darwin</a> platforms.  Within this environment, PyObjC can be used to entirely replace Objective-C in the development of Cocoa based applications and Foundation based command line tools.</p>
<p>
We want to offer the same level of support for <a href="http://www.gnustep.org/">GnuStep</a>, but need volunteers with GnuStep experience to make that happen!
</p>

<table border="0" cellpadding="0" cellspacing="0" width="100%">
<tr valign="top"><td width="50%">

<h1>News</h1>

<?
// Include news items
include $fsroot."news/news.inc";
?>
<div align="right"><a href="<? print $root; ?>news/index.php">Older News...</a></div>


</td><td>&nbsp;&nbsp;&nbsp;</td><td width="50%">

<h1>Status</h1>

<p>
<a href="http://sourceforge.net/project/showfiles.php?group_id=14534">PyObjC 0.8</a> was released on 19 December 2002.  See the <a href="http://cvs.sourceforge.net/cgi-bin/viewcvs.cgi/pyobjc/pyobjc/ChangeLog?rev=1.58&only_with_tag=REL_20021219_0pt8&content-type=text/vnd.viewcvs-markup">ChangeLog</a> for details.
</p>

<h1>Resources</h1>

<p>
Support is currently limited to <a href="http://lists.sourceforge.net/mailman/listinfo/pyobjc-dev">the developer's mailing list</a>.
</p>

<p>
The PyObjC project is hosted by
<a href="http://sourceforge.net/">SourceForge</a>.
In addition to hosting this site and the downloads, SourceForge
provides the following resources for the project:
</p>
<ul>
<li><a href="http://sourceforge.net/projects/pyobjc/">Project page</a></li>
<li><a
href="http://sourceforge.net/tracker/?group_id=14534&amp;atid=114534">Bug tracker</a></li>
<li><a href="http://sourceforge.net/project/showfiles.php?group_id=14534">Files</a></li>
<li>CVS (<a href="http://cvs.sourceforge.net/cgi-bin/viewcvs.cgi/pyobjc">browse online</a>, <a href="http://sourceforge.net/cvs/?group_id=14534">access instructions</a>)</li>

</ul>

</td></tr></table>


<?
include "footer.inc";
?>
