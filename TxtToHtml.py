# -*- coding:utf-8 -*-
import sys
import re
import urllib

def main():
	fileName = sys.argv[1]
	HtmlName = fileName.split('.')[0]+'.sanae'
	sourcefile = open(fileName)
	fp = open(HtmlName,'w')
	hasPre = False
	hasSCode = False
	hasImg = False
	
	for line in sourcefile:
		##code 代表是代码区，一般来说，使用<code>代码</code>的格式
		if line == '<code>\n':
			fp.write('<div>'+'\n')
			fp.write('''<pre class="brush: python;ruler: true">\n''')
			hasPre = True
			continue
		##代码区结束
		elif line == '</code>\n':
			fp.write('</pre>\n')
			fp.write('</div>'+'\n')
			hasPre = False
			continue
		elif hasPre:
			fp.write(line)
			continue
		##小代码区……估计一般用不上的
		elif line == '<scode>\n':
			hasSCode = True
			continue
		elif line == '</scode>\n':
			hasSCode = False	
			continue
		elif hasSCode:
			fp.write(ShCodePrecessor(line))
			continue
		elif line == '<img>\n':
			hasImg = True
			continue
		elif line == '</img>\n':
			hasImg = False
			continue
		elif hasImg:
			fp.write(ImgPrecessor(line))
		else:
			fp.write(ProcessedLine(line))
	fp.close()

def ImgPrecessor(line):
	line = line.strip('\n')
	line = line.strip('<').strip('>')
	line = line.split(' ')
	pro_line = ' '.join(i for i in line)
	pro_line = '<p><div align="center"><span><img '+pro_line+' /></span></div></p>\n'
	return pro_line
	
def ShCodePrecessor(line):
	line = replaceBlank(line)
	prefix = '''<p><span style="font-family:'Comic Sans MS';font-size:medium;color:#000099;">'''
	surfix = '''</span></p>'''
	line = line.strip('\n')
	line = prefix + line + surfix + '\n'
	return line

def replaceBlank(line):
	partern =re.compile(r'(\s+)\S*')
	if partern.match(line):
		blank = partern.match(line).group(1)
		line = '&nbsp;'*len(blank)+line[len(blank):]
	return line


def ProcessedLine(line):
	repDict = {
##	'</scode>:':'</span>',
##	'<scode>':'''<span style="font-family:'Comic Sans MS';font-size:medium;color:#000099;">''',
	'</href>':'</a>',
	'<href':'<a href'
			}
	line=replaceBlank(line)
	line = line.strip('\n')
	##这里的代码实现了链接的文字转成html标准形式
	##解析链接
	rehref = re.compile(r'<href="(.+?)">') 
	sourcelink = rehref.findall(line)
	destlink = [urllib.quote(i) for i in sourcelink]
	for i in zip(sourcelink,destlink):
		line = line.replace(i[0],i[1])
		line = line.replace('%3A',':')
##	splitRe = re.compile(r'<scode>.+</scode>')
##	splitStr = splitRe.findall(line)
##	if splitStr:
##		splitLine = line.split(splitStr)
##	else:
##		splitLine = line.split()
	

	
##	for i in splitLine:
##		pre = '''<span style="font-family:'Microsoft YaHei';font-size:medium;"><span
##		style="color:#333333;">'''
##		pro = '''</span>'''
##		i = pre + i + pro
	
	
	
	for key in repDict:
		line = line.replace(key,repDict[key])
	
	pre = '''<p><span style="font-family:'Microsoft YaHei';font-size:medium;color:#333333;">'''
	pro = '''</span></p>\n'''
	line = pre + line + pro
	return line
	
if __name__ == "__main__":
	main()
