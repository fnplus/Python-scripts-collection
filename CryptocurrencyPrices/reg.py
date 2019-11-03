import re

text = """<div class="ChartPriceHeader__BigAmount-sc-9ry7zl-4 dKeshi"><span>$9,170.63</span></div>
"""
pattern = re.compile(r"(\$\d+,\d+|\.\d+)")
regex = pattern.search(text)
print(regex)
