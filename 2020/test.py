

import re 
data = 'iyr:2016 hcl:#cfa07d eyr:2026 hgt:151cm pid:394185014 ecl:grn byr:1974'


m = re.search("hgt:(.*?)' '", data)

print(m)

	