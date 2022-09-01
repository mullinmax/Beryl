title:test page

# Markdown: Syntax

[TOC]

----



### Headers


Optionally, you may "close" atx-style headers. This is purely
cosmetic -- you can use this if you think it looks better. The
closing hashes don't even need to match the number of hashes
used to open the header. (The number of opening hashes
determines the header level.)

### Tables

#### example table
|a  |b  |
|---|---|
|  1|  2|
|  3|  4|

#### with no header

|   |   |
|---|---|
|  1|  2|

#### with no rows

|a  |b  |
|---|---|
|   |   |

#### Table with alignment

| Item      | Value |
| --------- | -----:|
| Computer  | $1600 |
| Phone     |   $12 |
| Pipe      |    $1 |

### Blockquotes

Markdown uses email-style `>` characters for blockquoting. If you're
familiar with quoting passages of text in an email message, then you
know how to create a blockquote in Markdown. It looks best if you hard
wrap the text and put a `>` before every line:

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

Markdown allows you to be lazy and only put the `>` before the first
line of a hard-wrapped paragraph:

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

Blockquotes can be nested (i.e. a blockquote-in-a-blockquote) by
adding additional levels of `>`:

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

Blockquotes can contain other Markdown elements, including headers, lists,
and code blocks:

> ## This is a header.
> 
> 1.   This is the first list item.
> 2.   This is the second list item.
> 
> Here's some example code:
> 
>     return shell_exec("echo $input | $markdown_script");

Any decent text editor should make email-style quoting easy. For
example, with BBEdit, you can make a selection and choose Increase
Quote Level from the Text menu.


### Lists

- first item in list
- second item in list
    - sub-item in list
    - other sub-item in list
- third item in list

### Code Blocks

inline ```code_block()```

```python
def hw():
    print('hello world')
```

## Span Elements

### Links

This is [an example](http://example.com/) inline link.

This is a footer[^1](http://example.net/)

### Emphasis

*single asterisks*

**double asterisks**