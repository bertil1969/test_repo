#!/usr/bin/env python3
from datetime import datetime

birthday = datetime(1969,9,9)

string=f'Bertil has a birthday on {birthday:%B %d, %Y}'
print(string)

f1=3.2271237738
print(f'Float number is {f1:.4f}')
print(f'Float number is {f1:03.5f}')

int1=12
print(f'Integer number is {int1:03}')

