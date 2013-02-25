AproSanae-s-Scripts
-------------------

__Some python scripts which I wrote.__


开这个repo的契机是[reverland](https://github.com/reverland)的某个repo。我觉得这挺有趣的。碎片式的代码我这里拖拖拉拉的，貌似也不少，所谓鸡肋代码？总之，感谢 @reverland 的好主意。

## Python

__TxtToHtml.py__
* A script to convert txt file to html format
* It was writed to make write blogs become convenient
* Usage: python TxtToHtml.py yourfile and will generate  
  a file which name is yourfile.sanae open and copy it
* You can use these gammers:  

```python
# To insert codes.Default is python
<code>
somecodes
</code>
# Short Codes
<scode>
somecodes
</scode>
# Content.Defalut is MS YaHei
I am a robot
# Insert image.You can ignore width and height
# But if you get a width,the image will be center
<img>
<src="the link" width="xxx" height="xxx">
</img>
# Insert link
<href="the link">title</href>
```

* PS: When I wrote the script,I was not even heard makedown  
  so the gammers which I used was not so wise and confuse :-)
