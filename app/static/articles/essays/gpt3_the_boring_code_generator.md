title:GPT-3: The Boring Code Generator

# GPT-3: The Boring Code Generator

[TOC]

GPT-3, a text-based AI from [OpenAI](https://openai.com/) that's available to the public and has some pretty incredible tricks up it's sleve. If you don't feel like writing code to interact with the GPT-3 API you can use [The Playground](https://beta.openai.com/playground) on OpenAI's website. If you haven't already I encourage you to try some of the prompts in this essay for yourself. You will need to create an account, but at the time of writing doing so gives you $18 of free credit which will last you much longer than you might suspect. Throughout this essay when I use GPT-3, I will show my prompts
>    like this

and GPT-3's output

    :::text
    like this

so a full prompt will looks like:

> Short title ideas for and essay about programming using a text AI program called GPT-3 to generate the boring code. Funny titles preferred:

    :::text
    1. "GPT-3: The Boring Code Generator"
    2. "GPT-3: The Code That Bore Me to Death"
    3. "GPT-3: The Most Boring Code in the World"
    4. "GPT-3: The Code That Put Me to Sleep"
    5. "GPT-3: The Code That Made Me Drowsy"
    6. "GPT-3: The Code That Made My Eyes Glaze Over"
    7. "GPT-3: The Code That I Will Never Use Again"

Hopefully two things are jumping out at you right now. 1.) This Essay was named by GPT-3 2.) It seems to understand what "funny" is. GPT-3 can do these complex things because it was trained on massive dataset. The dataset is so large that the entirety of wikipedia makes up a measly 3%.[^1] 

## Why Would I Use GPT-3 to Program?

While the end result of programming can be beautiful or exciting, there's frequently a lot of boring code. Here's an example where we are writing a simple python function that capitalizes strings:

```python
def fix_capitalization(input):
    words = input.split(' ')
    return ' '.join([w[0].upper()+w[1:].lower() for w in words])

fix_capitalization('an exAMplE StrIng')
>>> 'An Example String'
```

This funciton isn't terribly difficult to write but it does take some time and effort. However, there's something we've missed that GPT-3 can help with:

>write a python function that capitalizes each word in a string:

```python
def fix_capitalization(string):
    return string.title()
```
GPT-3 knew that there was a built-in funciton that could achaive what we wanted. But can it write it's own if there wasn't a built-in?

>write a python function that capitalizes each word in a string without using the str.title() or the str.capitalize() function:
```python
def title_case(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))
```
No sweat! But, what I'm not showing you is the handful of times I needed to run this prompt to get the results I wanted. So while this does work, you still need to check GPT-3's work carefully. This would be a great time to do test driven development.

## Where GPT-3 Excells


>write a python function that can extract part numbers from part codes. See examples bellow:
>part code -> part number
>BZX112483Y -> 112483
>009378AA -> 009378
>009-378AA -> 009378
>
>def get_part_number(part_code:str)-> str:
```python
    """Return part number from a part code.

    Args:
        part_code(str): String with the code

    Returns:
        The part number string

    """
    no_dash_part_code = part_code.replace('-','')
    alphas = [char for char in no_dash_part_code if char.isalpha()]
    return ''.join(alphas)
```

This output is particularly nice because not only does it robustly do what was implied, it also wrote documented code. You'll notice I started the function for it with type hints. I find that prompting it with a well formed function definition tends to lead to better output. If you think about how this is working that makes sense; GPT-3 doesn't **understand** python, it's just mimicing what comes next. So if your prompt looks more professional it's going to try to match that.

Now something I should point out is that GPT-3 isn't python specific. You can swap python for another langauge like T-SQL and still get good output.

>write a T-SQL function that can extract part numbers from part codes. See examples bellow:
>part code -> part number
>BZX112483Y -> 112483
>009378AA -> 009378
>009-378AA -> 009378
```SQL
CREATE FUNCTION extractPartNumber (@partText VARCHAR(100))
RETURNS VARCHAR(100)

BEGIN 

RETURN (
SELECT
CASE
WHEN CHARINDEX('-', @partText) = 0 THEN
    SUBSTRING(@partText, PATINDEX('%[0-9]%', @partText), LEN(@partText))
ELSE
    SUBSTRING(@partText, PATINDEX('%[0-9]%', @partText), CHARINDEX('-', @partText)-1)
END
)

END
```



## Sources
[^1]:[https://en.wikipedia.org/wiki/GPT-3](https://en.wikipedia.org/wiki/GPT-3)




~~~~
def fix_capitalization(input):
    words = input.split(' ')
    return ' '.join([w[0].upper()+w[1:].lower() for w in words])

fix_capitalization('an exAMplE StrIng')
>>> 'An Example String'
~~~~

~~~~.html
<p>HTML Document</p>
~~~~