# x2y
## A highly modular static templating engine.
#### Focused on generating static sites and documentation with shortcodes. 
### Example Markup:
```HTML
{{HEADER}}
<p>Site Content.</p>
<div class="foo">This is regular HTML</div>
{{BOLD-RED}}THIS IS SPECIAL BOLD RED TEXT{{/BOLD-RED}}
{{FOOTER}}
```
### What are shortcodes?
"Short Codes" are custom modular pieces of HTML/JS/CSS that can be inserted into your pages wherever you need them to go. 

In the above example, at the very top we see the ```{{HEADER}}``` shortcode. When you run **x2y** and sees the shortcode it will convert it into the the corresponding user defined code which might look something like this:
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

**Note:** The "output" directory will be created in the same directory as "main.py" if it doesn't already exist. 

