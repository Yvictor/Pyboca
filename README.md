# Pyboca
Python api 外交部中文名字轉拼音
### 安裝 installation
```
pip install pyboca
```

### Quickstart
```python
import pyboca
import pandas as pd
```


```python
pyboca.ch2en("王小明")
```




    'WANG,HSIAO-MING'




```python
pyboca.ch2en("王小明", encode='漢語')
```

    Only support ['漢語拼音', '通用拼音', '威妥瑪(WG)拼音', '國音第二式拼音'].



```python
pyboca.ch2en("王小明", encode='漢語拼音')
```




    'WANG,XIAO-MING'




```python
df = pd.read_csv('datasets/example.csv')
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>person_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>張家恬</td>
      <td>D291998842</td>
    </tr>
    <tr>
      <th>1</th>
      <td>王靖雯</td>
      <td>H194408089</td>
    </tr>
    <tr>
      <th>2</th>
      <td>林靜宏</td>
      <td>H295803811</td>
    </tr>
    <tr>
      <th>3</th>
      <td>張美君</td>
      <td>E194714552</td>
    </tr>
    <tr>
      <th>4</th>
      <td>高駿貴</td>
      <td>F198021497</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['en_name'] = df['name'].map(lambda name:pyboca.ch2en(name))
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>person_id</th>
      <th>en_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>張家恬</td>
      <td>D291998842</td>
      <td>CHANG,CHIA-TIEN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>王靖雯</td>
      <td>H194408089</td>
      <td>WANG,CHING-WEN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>林靜宏</td>
      <td>H295803811</td>
      <td>LIN,CHING-HUNG</td>
    </tr>
    <tr>
      <th>3</th>
      <td>張美君</td>
      <td>E194714552</td>
      <td>CHANG,MEI-CHUN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>高駿貴</td>
      <td>F198021497</td>
      <td>KAO,CHUN-KUEI</td>
    </tr>
    <tr>
      <th>5</th>
      <td>林昕啟</td>
      <td>H191737341</td>
      <td>LIN,HSIN-CHI</td>
    </tr>
    <tr>
      <th>6</th>
      <td>李宜潔</td>
      <td>F294348551</td>
      <td>LI,I-CHIEH</td>
    </tr>
    <tr>
      <th>7</th>
      <td>唐初名</td>
      <td>A295890915</td>
      <td>TANG,CHU-MING</td>
    </tr>
    <tr>
      <th>8</th>
      <td>賴聿名</td>
      <td>C296038555</td>
      <td>LAI,YU-MING</td>
    </tr>
    <tr>
      <th>9</th>
      <td>林威依</td>
      <td>H196003215</td>
      <td>LIN,WEI-I</td>
    </tr>
    <tr>
      <th>10</th>
      <td>林向瑄</td>
      <td>H294636343</td>
      <td>LIN,HSIANG-HSUAN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>賴建弘</td>
      <td>G294921060</td>
      <td>LAI,CHIEN-HUNG</td>
    </tr>
    <tr>
      <th>12</th>
      <td>林明倫</td>
      <td>B294449184</td>
      <td>LIN,MING-LUN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>劉萱生</td>
      <td>F294268352</td>
      <td>LIU,HSUAN-SHENG</td>
    </tr>
    <tr>
      <th>14</th>
      <td>韓瑋婷</td>
      <td>H194459273</td>
      <td>HAN,WEI-TING</td>
    </tr>
    <tr>
      <th>15</th>
      <td>倪舒以</td>
      <td>B197405557</td>
      <td>NI,SHU-I</td>
    </tr>
    <tr>
      <th>16</th>
      <td>陳淑忠</td>
      <td>F197667300</td>
      <td>CHEN,SHU-CHUNG</td>
    </tr>
    <tr>
      <th>17</th>
      <td>林亮丞</td>
      <td>A295814004</td>
      <td>LIN,LIANG-CHENG</td>
    </tr>
    <tr>
      <th>18</th>
      <td>陳信秀</td>
      <td>D291184857</td>
      <td>CHEN,HSIN-HSIU</td>
    </tr>
    <tr>
      <th>19</th>
      <td>魏佩珊</td>
      <td>A199068506</td>
      <td>WEI,PEI-SHAN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>楊佳琪</td>
      <td>H295286463</td>
      <td>YANG,CHIA-CHI</td>
    </tr>
    <tr>
      <th>21</th>
      <td>謝志瑋</td>
      <td>C199003285</td>
      <td>HSIEH,CHIH-WEI</td>
    </tr>
    <tr>
      <th>22</th>
      <td>吳政軍</td>
      <td>E195284142</td>
      <td>WU,CHENG-CHUN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>林嘉玲</td>
      <td>B294371832</td>
      <td>LIN,CHIA-LING</td>
    </tr>
    <tr>
      <th>24</th>
      <td>謝珮雄</td>
      <td>G193221238</td>
      <td>HSIEH,PEI-HSIUNG</td>
    </tr>
    <tr>
      <th>25</th>
      <td>楊文琳</td>
      <td>C194689267</td>
      <td>YANG,WEN-LIN</td>
    </tr>
    <tr>
      <th>26</th>
      <td>唐志軒</td>
      <td>D299747561</td>
      <td>TANG,CHIH-HSUAN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>洪淑娟</td>
      <td>A294154750</td>
      <td>HUNG,SHU-CHUAN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>張廷江</td>
      <td>H299453415</td>
      <td>CHANG,TING-CHIANG</td>
    </tr>
    <tr>
      <th>29</th>
      <td>袁怡孜</td>
      <td>C296185362</td>
      <td>YUAN,I-TZU</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>70</th>
      <td>彭智翔</td>
      <td>G192599844</td>
      <td>PENG,CHIH-HSIANG</td>
    </tr>
    <tr>
      <th>71</th>
      <td>林建智</td>
      <td>B198546968</td>
      <td>LIN,CHIEN-CHIH</td>
    </tr>
    <tr>
      <th>72</th>
      <td>吳雅琳</td>
      <td>B193962739</td>
      <td>WU,YA-LIN</td>
    </tr>
    <tr>
      <th>73</th>
      <td>劉毅劭</td>
      <td>C197265198</td>
      <td>LIU,I-SHAO</td>
    </tr>
    <tr>
      <th>74</th>
      <td>潘美惠</td>
      <td>B298127901</td>
      <td>PAN,MEI-HUI</td>
    </tr>
    <tr>
      <th>75</th>
      <td>陳盈珍</td>
      <td>C193906376</td>
      <td>CHEN,YING-CHEN</td>
    </tr>
    <tr>
      <th>76</th>
      <td>林嘉芷</td>
      <td>H292532959</td>
      <td>LIN,CHIA-CHIH</td>
    </tr>
    <tr>
      <th>77</th>
      <td>林守惟</td>
      <td>E296666186</td>
      <td>LIN,SHOU-WEI</td>
    </tr>
    <tr>
      <th>78</th>
      <td>吳政岑</td>
      <td>E298232848</td>
      <td>WU,CHENG-TSEN</td>
    </tr>
    <tr>
      <th>79</th>
      <td>臧健豪</td>
      <td>C198360932</td>
      <td>TSANG,CHIEN-HAO</td>
    </tr>
    <tr>
      <th>80</th>
      <td>王秀瑞</td>
      <td>B297539247</td>
      <td>WANG,HSIU-JUI</td>
    </tr>
    <tr>
      <th>81</th>
      <td>李政侑</td>
      <td>C298627158</td>
      <td>LI,CHENG-YU</td>
    </tr>
    <tr>
      <th>82</th>
      <td>陳慧珊</td>
      <td>F294194893</td>
      <td>CHEN,HUI-SHAN</td>
    </tr>
    <tr>
      <th>83</th>
      <td>賴佳雯</td>
      <td>G295856348</td>
      <td>LAI,CHIA-WEN</td>
    </tr>
    <tr>
      <th>84</th>
      <td>楊惠靖</td>
      <td>A296304623</td>
      <td>YANG,HUI-CHING</td>
    </tr>
    <tr>
      <th>85</th>
      <td>郭新倩</td>
      <td>F299186113</td>
      <td>KUO,HSIN-CHIEN</td>
    </tr>
    <tr>
      <th>86</th>
      <td>黃瓊文</td>
      <td>C293955095</td>
      <td>HUANG,CHIUNG-WEN</td>
    </tr>
    <tr>
      <th>87</th>
      <td>周之欣</td>
      <td>B291105185</td>
      <td>CHOU,CHIH-HSIN</td>
    </tr>
    <tr>
      <th>88</th>
      <td>蔡裕南</td>
      <td>E299620299</td>
      <td>TSAI,YU-NAN</td>
    </tr>
    <tr>
      <th>89</th>
      <td>沈惠玲</td>
      <td>A191868228</td>
      <td>SHEN,HUI-LING</td>
    </tr>
    <tr>
      <th>90</th>
      <td>黃建成</td>
      <td>H293797445</td>
      <td>HUANG,CHIEN-CHENG</td>
    </tr>
    <tr>
      <th>91</th>
      <td>周曼容</td>
      <td>E294941917</td>
      <td>CHOU,MAN-JUNG</td>
    </tr>
    <tr>
      <th>92</th>
      <td>蔡雅鈴</td>
      <td>C292238399</td>
      <td>TSAI,YA-LING</td>
    </tr>
    <tr>
      <th>93</th>
      <td>陳凡新</td>
      <td>F197096043</td>
      <td>CHEN,FAN-HSIN</td>
    </tr>
    <tr>
      <th>94</th>
      <td>劉家豪</td>
      <td>B291260841</td>
      <td>LIU,CHIA-HAO</td>
    </tr>
    <tr>
      <th>95</th>
      <td>洪嘉枝</td>
      <td>B193443659</td>
      <td>HUNG,CHIA-CHIH</td>
    </tr>
    <tr>
      <th>96</th>
      <td>阮湖銘</td>
      <td>E297864506</td>
      <td>JUAN,HU-MING</td>
    </tr>
    <tr>
      <th>97</th>
      <td>曹哲韋</td>
      <td>B297510724</td>
      <td>TSAO,CHE-WEI</td>
    </tr>
    <tr>
      <th>98</th>
      <td>李明岑</td>
      <td>H294769356</td>
      <td>LI,MING-TSEN</td>
    </tr>
    <tr>
      <th>99</th>
      <td>柳山哲</td>
      <td>H293622498</td>
      <td>LIU,SHAN-CHE</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 3 columns</p>
</div>



