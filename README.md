# x2y
## A highly modular static templating engine.
#### Focused on generating static sites and documentation with shortcodes.
#### Requires no external dependencies & is invisible on the front-end :) 
### Example Markup:
```HTML
{{HEADER}}
{{CARD}}
{{TITLE}}WELCOME{{/TITLE}}
This is demo content for x2y! Just some regular HTML here!</br>
<img src="img/bot.png">
{{/CARD}}
{{FOOTER}}
```
### Example Output:
```html
<!--HEADER-->
<!DOCTYPE html>
<html>
<body>
	<h1>x2y</h2>
	<div class="navigation">
		<a href="https://example.com/index.html">Home</a>
		<a href="https://example.com/projects/test.html">Test</a>
	</div>
	
<div class="card">
<h2 class="title">WELCOME</h2>
This is demo content for x2y! Just some regular HTML here!</br>
<img src="img/bot.png">
</div>
<!--FOOTER-->
<div class="footer"><a href="https://github.com/matdombrock/x2y">Checkout x2y on Github!</a></div>
</body>
<link rel="stylesheet" href="https://example.com/styles.css">
</html>
```
### What are shortcodes?
"Short Codes" or "shortcodes" are custom modular pieces of HTML/JS/CSS that can be inserted into your pages wherever you need them to go. 

In the above example, at the very top we see the ```{{HEADER}}``` shortcode. When you run **x2y** and it sees the shortcode it will convert it into the the corresponding user defined code which might look something like this:
```HTML
<!--HEADER-->
<!DOCTYPE html>
<html>
<body>
	<h1>SITE TITLE</h2>
```
### Why use shortcodes?
The main benefit of using a shortcode system on static sites is that when it comes time to make a change to a major part of your site, for instance the navigation bar, you will not need to manually edit every single page on your site to include the new code (or cross your fingers that your regular expressions will really work this time). 

### How to make a template:
The template specifies both the structural layout and content for your site. It will contain all of the HTML files that you need to process and include in your final site. It will also act as a representation of the final directory structure. The files in the "template" directory will contain all of your site content, things like articles, blog posts, the home page ect.

Any files that you place into the "template" directory will automatically become part of your 'site template'. When you run this software it will walk through the "template" directory, replacing shortcodes with their expanded counterparts and sending the new copies to the "output" directory. All internal directory structure (inside of the "template" directory) will be preserved in the "output" directory. 

**Note:** *By default, the software will only parse HTML files. Any other types of files that you include in your template directory such as images, CSS ect. will not be parsed, it will simply be copied over to the "output" directory. There is really no reason that you need to include any other file types in your "template" directory, and it will slightly slow down the software, but some users might find this much simpler and easier than manually merging the exported template with the rest of their site files.* 

Anything that you can normally do with front-end web technologies should work here including loading external libraries. For the most part, building the template will be very similar to writing a traditional static website, except now you will have the power of shortcodes at your disposal. If you have ever worked with the shortcode system in WordPress you should feel right at home here. 

The existing "template" directory contains some very basic examples of how you might structure your own template directory.  

### How to create a new shortcode:
Creating and adding new shortcodes is a fairly straight forward process. 

First create a new HTML file in the "shortcodes" directory. 

**Note:** *This is not the "shortcodes.py" file, but we will need to edit that as well momentarily. The name of this new file doesn't matter but you will need to remember it in just a moment when we add it to the "shortcodes.py" file.* 

In this newly created file, you can add whatever HTML/JS/CSS that you might need. 

**WARNING:** *To ensure that the shortcode is truly modular, you should **only use absolute links!***

For example:
```
http://example.com/ --OK!
http://example.com/path/ --OK!
http://example.com/path/to/some/file.html --OK!
/path/ --PROBABLY NOT OK!
/path/to/some/file.html --PROBABLY NOT OK!
```

**TIP**: *You can set a custom root URL in "config.py". This will allow you to use the special syntax ```[[URL]]``` in your shortcodes like this:*
```html
<div class="navigation">
		<a href="[[URL]]index.html">Home</a>
		<a href="[[URL]]projects/test.html">Test</a>
</div>
```
or:
```html
<link rel="stylesheet" href="[[URL]]styles.css">
```

Once you have created the shortcode file and saved it as something like ```NewShortCodeName.html``` inside of the "shortcodes" directory, you need to make sure the software knows what it is by adding it to "shortcodes.py". This  file contains a dictionary of every shortcode's name and its relative location inside of the "shortcodes" directory. 

You can add your new shortcode anywhere after the line containing:

```defs = {}```

For example, you might add a new shortcode named "NAVIGATION" like this:

```defs.update({"NAVIGATION":"navigation.html"})```

To include this new shortcode in one of your templates you would simply insert the code```{{NAVIGATION}}``` into the desired location(s) in your HTML.

### Generating the site:
Generating the site from your template is really easy. Just run the "main.py" file with something like:

```python3 main.py```

If all goes well your new site will be located in the "output" directory. 

**Note:** *The "output" directory will be created in the same directory as "main.py" if it doesn't already exist.*
**Note:** *By default, this software will only parse html files. That is files ending in ".htm" or ".html" (Case insensitive). You can change which file types will be parsed by editing the ```parse_types``` variable in "config.py". This was done to prevent the software from attempting to parse things such as images and audio.* 

### Configuration:
All configuration happens in the "config.py" file. Soon I will add support for command line arguments.
At the time of writing, the "config.py" file looks like this:
```python
url = "https://example.com" #no trailing slash
parse_types = "html, htm"#separate with spaces
shortcode_location = "shortcodes"
output_location = "output"
template_location = "template"
auto_purge = False
```
**URL:** Sets the base URL for the site. This is really useful when you need to quickly switch between deploying to a live and static server quickly. 

**PARSE_TYPES:** Determines which file types should be parsed by the application. The default should be enough for most web sites. This functionality is in place to allow for this software to be used in this like text or CSV processing as well as HTML. 

**SHORTCODE_LOCATION:** Sets the directory location for the shortcodes directory. Allows for quick A/B testing of shortcodes. 

**OUTPUT_LOCATION:** Sets the output directory location. Useful for exporting variations of the template. 

**TEMPLATE_LOCATION:** Sets the template directory location. Useful if you have multiple sites sharing the same set of shortcodes. 

**AUTO_PURGE**
Determines if the software should ask the user before purging the current output location. By default the software will prompt the user for a  yes/no response before purging. If set to ```True``` this prompt will be skipped. 

### TODO:
-Add CLI parameter options

-Support Markdown to HTML conversion