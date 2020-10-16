import requests
from html.parser import HTMLParser
import urllib.parse
import datetime
import re
import os

class MyHTMLParser(HTMLParser):
    value=''
    dict_att={}
    def handle_starttag(self, tag, attrs):
        self.dict_att=dict(attrs)
        if 'name' in self.dict_att and 'id' in self.dict_att and self.dict_att['name']=='__VIEWSTATE' and self.dict_att['id']=='__VIEWSTATE':
            self.value=self.dict_att['value']



class GetUndoReport(HTMLParser):
    regex = r"(....-..-..)(?=\(未填报，请点击此处补报\))"
    date_list=[]
    a=[]
    def handle_data(self, data):
        a=re.findall(self.regex,data,re.MULTILINE)
        if a:
            self.date_list=a



url="https://newsso.shu.edu.cn/login"
headers={
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "https://newsso.shu.edu.cn",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Referer": "https://newsso.shu.edu.cn/login",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

header_g={
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding":"gzip, deflate,br",
    "Accept-Language":"zh-CN,zh;q=0.9"
}
userpass={
    "username":"18122133",
    "password":"Oliver23",
    "login_submit":"登录"
}


data_p={
    "__EVENTTARGET" : "p1$ctl00$btnSubmit" ,
    "__EVENTARGUMENT" : "" ,
    "__VIEWSTATEGENERATOR" : "7AD7E509" ,
    "p1$ChengNuo" : "p1_ChengNuo" ,
    "p1$DangQSTZK" : "良好" ,
    "p1$TiWen" : "37" ,
    "p1$JiuYe_ShouJHM" : "" ,
    "p1$JiuYe_Email" : "" ,
    "p1$JiuYe_Wechat" : "" ,
    "p1$QiuZZT" : "" ,
    "p1$JiuYKN" : "" ,
    "p1$JiuYSJ" : "" ,
    "p1$ZaiXiao" : "不在校" ,
    "p1$MingTDX" : "不到校" ,
    "p1$BanChe_1$Value" : "0" ,
    "p1$BanChe_1" : "不需要乘班车" ,
    "p1$BanChe_2$Value" : "0" ,
    "p1$BanChe_2" : "不需要乘班车" ,
    "p1$GuoNei" : "国内" ,
    "p1$ddlGuoJia$Value" : "-1" ,
    "p1$ddlGuoJia" : "选择国家" ,
    "p1$ddlSheng$Value" : "上海" ,
    "p1$ddlSheng" : "上海" ,
    "p1$ddlShi$Value" : "上海市" ,
    "p1$ddlShi" : "上海市" ,
    "p1$ddlXian$Value" : "浦东新区" ,
    "p1$ddlXian" : "浦东新区" ,
    "p1$FengXDQDL" : "否" ,
    "p1$TongZWDLH" : "否" ,
    "p1$XiangXDZ" : "利津路555弄11号101室" ,
    "p1$QueZHZJC$Value" : "否" ,
    "p1$QueZHZJC" : "否" ,
    "p1$DangRGL" : "否" ,
    "p1$GeLDZ" : "" ,
    "p1$FanXRQ" : "" ,
    "p1$WeiFHYY" : "" ,
    "p1$ShangHJZD" : "" ,
    "p1$DaoXQLYGJ" : "" ,
    "p1$DaoXQLYCS" : "" ,
    "p1$CengFWH_RiQi" : "" ,
    "p1$CengFWH_BeiZhu" : "" ,
    "p1$JieChu_RiQi" : "" ,
    "p1$JieChu_BeiZhu" : "" ,
    "p1$TuJWH_RiQi" : "" ,
    "p1$TuJWH_BeiZhu" : "" ,
    "p1$JiaRen_BeiZhu" : "" ,
    "p1$SuiSM" : "绿色" ,
    "p1$LvMa14Days" : "是" ,
    "p1$Address2" : "" ,
    "F_TARGET" : "p1_ctl00_btnSubmit" ,
    "p1_BanCSM_Collapsed" : "false" ,
    "p1_GeLSM_Collapsed" : "false" ,
    "p1_Collapsed" : "false",
    "F_STATE" : r"eyJwMV9CYW9TUlEiOnsiVGV4dCI6IjIwMjAtMDgtMDEifSwicDFfRGFuZ1FTVFpLIjp7IkZfSXRlbXMiOltbIuiJr+WlvSIsIuiJr+WlvSIsMV0sWyLkuI3pgIIiLCLkuI3pgIIiLDFdXSwiU2VsZWN0ZWRWYWx1ZSI6IuiJr+WlvSJ9LCJwMV9aaGVuZ1podWFuZyI6eyJIaWRkZW4iOnRydWUsIkZfSXRlbXMiOltbIuaEn+WGkiIsIuaEn+WGkiIsMV0sWyLlkrPll70iLCLlkrPll70iLDFdLFsi5Y+R54OtIiwi5Y+R54OtIiwxXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6W119LCJwMV9RaXVaWlQiOnsiRl9JdGVtcyI6W10sIlNlbGVjdGVkVmFsdWVBcnJheSI6W119LCJwMV9KaXVZS04iOnsiRl9JdGVtcyI6W10sIlNlbGVjdGVkVmFsdWVBcnJheSI6W119LCJwMV9KaXVZWVgiOnsiUmVxdWlyZWQiOmZhbHNlLCJGX0l0ZW1zIjpbXSwiU2VsZWN0ZWRWYWx1ZUFycmF5IjpbXX0sInAxX0ppdVlaRCI6eyJGX0l0ZW1zIjpbXSwiU2VsZWN0ZWRWYWx1ZUFycmF5IjpbXX0sInAxX0ppdVlaTCI6eyJGX0l0ZW1zIjpbXSwiU2VsZWN0ZWRWYWx1ZUFycmF5IjpbXX0sInAxX1phaVhpYW8iOnsiRl9JdGVtcyI6W1si5LiN5Zyo5qChIiwi5LiN5Zyo5qChIiwxXSxbIuWuneWxsSIsIuWuneWxseagoeWMuiIsMV0sWyLlu7bplb8iLCLlu7bplb/moKHljLoiLDFdLFsi5ZiJ5a6aIiwi5ZiJ5a6a5qCh5Yy6IiwxXSxbIuaWsOmXuOi3ryIsIuaWsOmXuOi3r+agoeWMuiIsMV1dLCJTZWxlY3RlZFZhbHVlIjoi5LiN5Zyo5qChIn0sInAxX01pbmdURFgiOnsiU2VsZWN0ZWRWYWx1ZSI6IuS4jeWIsOagoSIsIkZfSXRlbXMiOltbIuS4jeWIsOagoSIsIuS4jeWIsOagoSIsMV0sWyLlrp3lsbEiLCLlrp3lsbHmoKHljLoiLDFdLFsi5bu26ZW/Iiwi5bu26ZW/5qCh5Yy6IiwxXSxbIuWYieWumiIsIuWYieWumuagoeWMuiIsMV0sWyLmlrDpl7jot68iLCLmlrDpl7jot6/moKHljLoiLDFdXX0sInAxX01pbmdUSkMiOnsiUmVxdWlyZWQiOmZhbHNlLCJIaWRkZW4iOnRydWUsIkZfSXRlbXMiOltbIuaYryIsIuaYryIsMV0sWyLlkKYiLCLlkKYiLDFdXSwiU2VsZWN0ZWRWYWx1ZSI6bnVsbH0sInAxX0JhbkNoZV8xIjp7IkhpZGRlbiI6dHJ1ZSwiRl9JdGVtcyI6W1siMCIsIuS4jemcgOimgeS5mOePrei9piIsMSwiIiwiIl0sWyIxIiwiMeWPt+e6v++8muWYieWumuagoeWMuuWNl+mXqD0+5a6d5bGx5qCh5Yy6IiwxLCIiLCIiXSxbIjIiLCIy5Y+357q/77ya5a6d5bGx5qCh5Yy6PT7lmInlrprmoKHljLrljZfpl6giLDEsIiIsIiJdLFsiMyIsIjPlj7fnur/vvJrlu7bplb/moKHljLrljJfpl6g9PuWuneWxseagoeWMuiIsMSwiIiwiIl0sWyI0IiwiNOWPt+e6v++8muWuneWxseagoeWMuj0+5bu26ZW/5qCh5Yy65YyX6ZeoIiwxLCIiLCIiXSxbIjUiLCI15Y+357q/77ya5ZiJ5a6a5qCh5Yy65Y2X6ZeoPT7lu7bplb/moKHljLrljJfpl6giLDEsIiIsIiJdLFsiNiIsIjblj7fnur/vvJrlu7bplb/moKHljLrljJfpl6g9PuWYieWumuagoeWMuuWNl+mXqCIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsiMCJdfSwicDFfQmFuQ2hlXzIiOnsiSGlkZGVuIjp0cnVlLCJGX0l0ZW1zIjpbWyIwIiwi5LiN6ZyA6KaB5LmY54+t6L2mIiwxLCIiLCIiXSxbIjEiLCIx5Y+357q/77ya5ZiJ5a6a5qCh5Yy65Y2X6ZeoPT7lrp3lsbHmoKHljLoiLDEsIiIsIiJdLFsiMiIsIjLlj7fnur/vvJrlrp3lsbHmoKHljLo9PuWYieWumuagoeWMuuWNl+mXqCIsMSwiIiwiIl0sWyIzIiwiM+WPt+e6v++8muW7tumVv+agoeWMuuWMl+mXqD0+5a6d5bGx5qCh5Yy6IiwxLCIiLCIiXSxbIjQiLCI05Y+357q/77ya5a6d5bGx5qCh5Yy6PT7lu7bplb/moKHljLrljJfpl6giLDEsIiIsIiJdLFsiNSIsIjXlj7fnur/vvJrlmInlrprmoKHljLrljZfpl6g9PuW7tumVv+agoeWMuuWMl+mXqCIsMSwiIiwiIl0sWyI2IiwiNuWPt+e6v++8muW7tumVv+agoeWMuuWMl+mXqD0+5ZiJ5a6a5qCh5Yy65Y2X6ZeoIiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyIwIl19LCJwMV9CYW5DU00iOnsiSGlkZGVuIjp0cnVlLCJJRnJhbWVBdHRyaWJ1dGVzIjp7fX0sInAxX0d1b05laSI6eyJGX0l0ZW1zIjpbWyLlm73lhoUiLCLlm73lhoUiLDFdLFsi5Zu95aSWIiwi5Zu95aSWIiwxXV0sIlNlbGVjdGVkVmFsdWUiOiLlm73lhoUifSwicDFfZGRsR3VvSmlhIjp7IkRhdGFUZXh0RmllbGQiOiJaaG9uZ1dlbiIsIkRhdGFWYWx1ZUZpZWxkIjoiWmhvbmdXZW4iLCJIaWRkZW4iOnRydWUsIkZfSXRlbXMiOltbIi0xIiwi6YCJ5oup5Zu95a62IiwxLCIiLCIiXSxbIumYv+WwlOW3tOWwvOS6miIsIumYv+WwlOW3tOWwvOS6miIsMSwiIiwiIl0sWyLpmL/lsJTlj4rliKnkupoiLCLpmL/lsJTlj4rliKnkupoiLDEsIiIsIiJdLFsi6Zi/5a+M5rGXIiwi6Zi/5a+M5rGXIiwxLCIiLCIiXSxbIumYv+agueW7tyIsIumYv+agueW7tyIsMSwiIiwiIl0sWyLpmL/mi4nkvK/ogZTlkIjphYvplb/lm70iLCLpmL/mi4nkvK/ogZTlkIjphYvplb/lm70iLDEsIiIsIiJdLFsi6Zi/6bKB5be0Iiwi6Zi/6bKB5be0IiwxLCIiLCIiXSxbIumYv+abvCIsIumYv+abvCIsMSwiIiwiIl0sWyLpmL/loZ7mi5znloYiLCLpmL/loZ7mi5znloYiLDEsIiIsIiJdLFsi5Z+D5Y+KIiwi5Z+D5Y+KIiwxLCIiLCIiXSxbIuWfg+WhnuS/hOavlOS6miIsIuWfg+WhnuS/hOavlOS6miIsMSwiIiwiIl0sWyLniLHlsJTlhbAiLCLniLHlsJTlhbAiLDEsIiIsIiJdLFsi54ix5rKZ5bC85LqaIiwi54ix5rKZ5bC85LqaIiwxLCIiLCIiXSxbIuWuiemBk+WwlCIsIuWuiemBk+WwlCIsMSwiIiwiIl0sWyLlronlk6Xmi4kiLCLlronlk6Xmi4kiLDEsIiIsIiJdLFsi5a6J5Zyt5ouJIiwi5a6J5Zyt5ouJIiwxLCIiLCIiXSxbIuWuieaPkOeTnOWSjOW3tOW4g+i+viIsIuWuieaPkOeTnOWSjOW3tOW4g+i+viIsMSwiIiwiIl0sWyLlpaXlnLDliKkiLCLlpaXlnLDliKkiLDEsIiIsIiJdLFsi5aWl5YWw576k5bKbIiwi5aWl5YWw576k5bKbIiwxLCIiLCIiXSxbIua+s+Wkp+WIqeS6miIsIua+s+Wkp+WIqeS6miIsMSwiIiwiIl0sWyLlt7Tlt7TlpJrmlq8iLCLlt7Tlt7TlpJrmlq8iLDEsIiIsIiJdLFsi5be05biD5Lqa5paw5Yeg5YaF5LqaIiwi5be05biD5Lqa5paw5Yeg5YaF5LqaIiwxLCIiLCIiXSxbIuW3tOWTiOmprCIsIuW3tOWTiOmprCIsMSwiIiwiIl0sWyLlt7Tln7rmlq/lnaYiLCLlt7Tln7rmlq/lnaYiLDEsIiIsIiJdLFsi5be05YuS5pav5Z2mIiwi5be05YuS5pav5Z2mIiwxLCIiLCIiXSxbIuW3tOaelyIsIuW3tOaelyIsMSwiIiwiIl0sWyLlt7Tmi7/pqawiLCLlt7Tmi7/pqawiLDEsIiIsIiJdLFsi5be06KW/Iiwi5be06KW/IiwxLCIiLCIiXSxbIueZveS/hOe9l+aWryIsIueZveS/hOe9l+aWryIsMSwiIiwiIl0sWyLnmb7mhZXlpKciLCLnmb7mhZXlpKciLDEsIiIsIiJdLFsi5L+d5Yqg5Yip5LqaIiwi5L+d5Yqg5Yip5LqaIiwxLCIiLCIiXSxbIui0neWugSIsIui0neWugSIsMSwiIiwiIl0sWyLmr5TliKnml7YiLCLmr5TliKnml7YiLDEsIiIsIiJdLFsi5Yaw5bKbIiwi5Yaw5bKbIiwxLCIiLCIiXSxbIuazouWkmum7juWQhCIsIuazouWkmum7juWQhCIsMSwiIiwiIl0sWyLms6LlhbAiLCLms6LlhbAiLDEsIiIsIiJdLFsi5rOi5pav5bC85Lqa5ZKM6buR5aGe5ZOl57u06YKjIiwi5rOi5pav5bC85Lqa5ZKM6buR5aGe5ZOl57u06YKjIiwxLCIiLCIiXSxbIueOu+WIqee7tOS6miIsIueOu+WIqee7tOS6miIsMSwiIiwiIl0sWyLkvK/liKnlhbkiLCLkvK/liKnlhbkiLDEsIiIsIiJdLFsi5Y2a6Iyo55Om57qzIiwi5Y2a6Iyo55Om57qzIiwxLCIiLCIiXSxbIuS4jeS4uSIsIuS4jeS4uSIsMSwiIiwiIl0sWyLluIPln7rnurPms5XntKIiLCLluIPln7rnurPms5XntKIiLDEsIiIsIiJdLFsi5biD6ZqG6L+qIiwi5biD6ZqG6L+qIiwxLCIiLCIiXSxbIuW4g+e7tOWymyIsIuW4g+e7tOWymyIsMSwiIiwiIl0sWyLmnJ3pspwiLCLmnJ3pspwiLDEsIiIsIiJdLFsi6LWk6YGT5Yeg5YaF5LqaIiwi6LWk6YGT5Yeg5YaF5LqaIiwxLCIiLCIiXSxbIuS4uem6piIsIuS4uem6piIsMSwiIiwiIl0sWyLlvrflm70iLCLlvrflm70iLDEsIiIsIiJdLFsi5Lic5bid5rG2Iiwi5Lic5bid5rG2IiwxLCIiLCIiXSxbIuS4nOW4neaxtiIsIuS4nOW4neaxtiIsMSwiIiwiIl0sWyLlpJrlk6UiLCLlpJrlk6UiLDEsIiIsIiJdLFsi5aSa57Gz5bC85YqgIiwi5aSa57Gz5bC85YqgIiwxLCIiLCIiXSxbIuS/hOe9l+aWr+iBlOmCpiIsIuS/hOe9l+aWr+iBlOmCpiIsMSwiIiwiIl0sWyLljoTnk5zlpJrlsJQiLCLljoTnk5zlpJrlsJQiLDEsIiIsIiJdLFsi5Y6E56uL54m56YeM5LqaIiwi5Y6E56uL54m56YeM5LqaIiwxLCIiLCIiXSxbIuazleWbvSIsIuazleWbvSIsMSwiIiwiIl0sWyLms5Xlm73lpKfpg73kvJoiLCLms5Xlm73lpKfpg73kvJoiLDEsIiIsIiJdLFsi5rOV572X576k5bKbIiwi5rOV572X576k5bKbIiwxLCIiLCIiXSxbIuazleWxnuazouWIqeWwvOilv+S6miIsIuazleWxnuazouWIqeWwvOilv+S6miIsMSwiIiwiIl0sWyLms5XlsZ7lnK3kuprpgqMiLCLms5XlsZ7lnK3kuprpgqMiLDEsIiIsIiJdLFsi5qK16JKC5YaIIiwi5qK16JKC5YaIIiwxLCIiLCIiXSxbIuiPsuW+i+WuviIsIuiPsuW+i+WuviIsMSwiIiwiIl0sWyLmlpDmtY4iLCLmlpDmtY4iLDEsIiIsIiJdLFsi6Iqs5YWwIiwi6Iqs5YWwIiwxLCIiLCIiXSxbIuS9m+W+l+inkiIsIuS9m+W+l+inkiIsMSwiIiwiIl0sWyLlhojmr5TkupoiLCLlhojmr5TkupoiLDEsIiIsIiJdLFsi5Yia5p6cIiwi5Yia5p6cIiwxLCIiLCIiXSxbIuWImuaenO+8iOmHke+8iSIsIuWImuaenO+8iOmHke+8iSIsMSwiIiwiIl0sWyLlk6XkvKbmr5TkupoiLCLlk6XkvKbmr5TkupoiLDEsIiIsIiJdLFsi5ZOl5pav6L6+6buO5YqgIiwi5ZOl5pav6L6+6buO5YqgIiwxLCIiLCIiXSxbIuagvOael+e6s+i+viIsIuagvOael+e6s+i+viIsMSwiIiwiIl0sWyLmoLzpsoHlkInkupoiLCLmoLzpsoHlkInkupoiLDEsIiIsIiJdLFsi5qC56KW/5bKbIiwi5qC56KW/5bKbIiwxLCIiLCIiXSxbIuWPpOW3tCIsIuWPpOW3tCIsMSwiIiwiIl0sWyLnk5zlvrfnvZfmma7lspsiLCLnk5zlvrfnvZfmma7lspsiLDEsIiIsIiJdLFsi5YWz5bKbIiwi5YWz5bKbIiwxLCIiLCIiXSxbIuWcreS6mumCoyIsIuWcreS6mumCoyIsMSwiIiwiIl0sWyLlk4jokKjlhYvmlq/lnaYiLCLlk4jokKjlhYvmlq/lnaYiLDEsIiIsIiJdLFsi5rW35ZywIiwi5rW35ZywIiwxLCIiLCIiXSxbIumfqeWbvSIsIumfqeWbvSIsMSwiIiwiIl0sWyLojbflhbAiLCLojbflhbAiLDEsIiIsIiJdLFsi6buR5bGxIiwi6buR5bGxIiwxLCIiLCIiXSxbIua0qumDveaLieaWryIsIua0qumDveaLieaWryIsMSwiIiwiIl0sWyLln7rph4zlt7Tmlq8iLCLln7rph4zlt7Tmlq8iLDEsIiIsIiJdLFsi5ZCJ5biD5o+QIiwi5ZCJ5biD5o+QIiwxLCIiLCIiXSxbIuWQieWwlOWQieaWr+aWr+WdpiIsIuWQieWwlOWQieaWr+aWr+WdpiIsMSwiIiwiIl0sWyLlh6DlhoXkupoiLCLlh6DlhoXkupoiLDEsIiIsIiJdLFsi5Yeg5YaF5Lqa5q+U57uNIiwi5Yeg5YaF5Lqa5q+U57uNIiwxLCIiLCIiXSxbIuWKoOaLv+WkpyIsIuWKoOaLv+WkpyIsMSwiIiwiIl0sWyLliqDnurMiLCLliqDnurMiLDEsIiIsIiJdLFsi5Yqg6JOsIiwi5Yqg6JOsIiwxLCIiLCIiXSxbIuafrOWflOWvqCIsIuafrOWflOWvqCIsMSwiIiwiIl0sWyLmjbflhYsiLCLmjbflhYsiLDEsIiIsIiJdLFsi5rSl5be05biD6Z+mIiwi5rSl5be05biD6Z+mIiwxLCIiLCIiXSxbIuWWgOm6pumahiIsIuWWgOm6pumahiIsMSwiIiwiIl0sWyLljaHloZTlsJQiLCLljaHloZTlsJQiLDEsIiIsIiJdLFsi56eR56eR5pav77yI5Z+65p6X77yJ576k5bKbIiwi56eR56eR5pav77yI5Z+65p6X77yJ576k5bKbIiwxLCIiLCIiXSxbIuenkeaRqee9lyIsIuenkeaRqee9lyIsMSwiIiwiIl0sWyLnp5Hnibnov6rnk6YiLCLnp5Hnibnov6rnk6YiLDEsIiIsIiJdLFsi56eR5aiB54m5Iiwi56eR5aiB54m5IiwxLCIiLCIiXSxbIuWFi+e9l+WcsOS6miIsIuWFi+e9l+WcsOS6miIsMSwiIiwiIl0sWyLogq/lsLzkupoiLCLogq/lsLzkupoiLDEsIiIsIiJdLFsi5bqT5YWL576k5bKbIiwi5bqT5YWL576k5bKbIiwxLCIiLCIiXSxbIuaLieiEsee7tOS6miIsIuaLieiEsee7tOS6miIsMSwiIiwiIl0sWyLojrHntKLmiZgiLCLojrHntKLmiZgiLDEsIiIsIiJdLFsi6ICB5oydIiwi6ICB5oydIiwxLCIiLCIiXSxbIum7juW3tOWrqSIsIum7juW3tOWrqSIsMSwiIiwiIl0sWyLnq4vpmbblrpsiLCLnq4vpmbblrpsiLDEsIiIsIiJdLFsi5Yip5q+U6YeM5LqaIiwi5Yip5q+U6YeM5LqaIiwxLCIiLCIiXSxbIuWIqeavlOS6miIsIuWIqeavlOS6miIsMSwiIiwiIl0sWyLliJfmlK/mlablo6vnmbsiLCLliJfmlK/mlablo6vnmbsiLDEsIiIsIiJdLFsi55WZ5bC85rGq5bKbIiwi55WZ5bC85rGq5bKbIiwxLCIiLCIiXSxbIuWNouajruWgoSIsIuWNouajruWgoSIsMSwiIiwiIl0sWyLljaLml7rovr4iLCLljaLml7rovr4iLDEsIiIsIiJdLFsi572X6ams5bC85LqaIiwi572X6ams5bC85LqaIiwxLCIiLCIiXSxbIumprOi+vuWKoOaWr+WKoCIsIumprOi+vuWKoOaWr+WKoCIsMSwiIiwiIl0sWyLpqazmganlspsiLCLpqazmganlspsiLDEsIiIsIiJdLFsi6ams5bCU5Luj5aSrIiwi6ams5bCU5Luj5aSrIiwxLCIiLCIiXSxbIumprOiAs+S7liIsIumprOiAs+S7liIsMSwiIiwiIl0sWyLpqazmi4nnu7QiLCLpqazmi4nnu7QiLDEsIiIsIiJdLFsi6ams5p2l6KW/5LqaIiwi6ams5p2l6KW/5LqaIiwxLCIiLCIiXSxbIumprOmHjCIsIumprOmHjCIsMSwiIiwiIl0sWyLpqazlhbbpob8iLCLpqazlhbbpob8iLDEsIiIsIiJdLFsi6ams57uN5bCU576k5bKbIiwi6ams57uN5bCU576k5bKbIiwxLCIiLCIiXSxbIumprOaPkOWwvOWFi+WymyIsIumprOaPkOWwvOWFi+WymyIsMSwiIiwiIl0sWyLpqaznuqbnibkiLCLpqaznuqbnibkiLDEsIiIsIiJdLFsi5q+b6YeM5rGC5pavIiwi5q+b6YeM5rGC5pavIiwxLCIiLCIiXSxbIuavm+mHjOWhlOWwvOS6miIsIuavm+mHjOWhlOWwvOS6miIsMSwiIiwiIl0sWyLnvo7lm70iLCLnvo7lm70iLDEsIiIsIiJdLFsi576O5bGe6JCo5pGp5LqaIiwi576O5bGe6JCo5pGp5LqaIiwxLCIiLCIiXSxbIuiSmeWPpCIsIuiSmeWPpCIsMSwiIiwiIl0sWyLokpnnibnloZ7mi4nnibkiLCLokpnnibnloZ7mi4nnibkiLDEsIiIsIiJdLFsi5a2f5Yqg5ouJIiwi5a2f5Yqg5ouJIiwxLCIiLCIiXSxbIuenmOmygSIsIuenmOmygSIsMSwiIiwiIl0sWyLlr4blhYvnvZflsLzopb/kupoiLCLlr4blhYvnvZflsLzopb/kupoiLDEsIiIsIiJdLFsi57yF55S4Iiwi57yF55S4IiwxLCIiLCIiXSxbIuaRqeWwlOWkmueTpiIsIuaRqeWwlOWkmueTpiIsMSwiIiwiIl0sWyLmkanmtJvlk6UiLCLmkanmtJvlk6UiLDEsIiIsIiJdLFsi5pGp57qz5ZOlIiwi5pGp57qz5ZOlIiwxLCIiLCIiXSxbIuiOq+ahkeavlOWFiyIsIuiOq+ahkeavlOWFiyIsMSwiIiwiIl0sWyLloqjopb/lk6UiLCLloqjopb/lk6UiLDEsIiIsIiJdLFsi57qz57Gz5q+U5LqaIiwi57qz57Gz5q+U5LqaIiwxLCIiLCIiXSxbIuWNl+mdniIsIuWNl+mdniIsMSwiIiwiIl0sWyLljZfmlq/mi4nlpKsiLCLljZfmlq/mi4nlpKsiLDEsIiIsIiJdLFsi55GZ6bKBIiwi55GZ6bKBIiwxLCIiLCIiXSxbIuWwvOaziuWwlCIsIuWwvOaziuWwlCIsMSwiIiwiIl0sWyLlsLzliqDmi4nnk5wiLCLlsLzliqDmi4nnk5wiLDEsIiIsIiJdLFsi5bC85pel5bCUIiwi5bC85pel5bCUIiwxLCIiLCIiXSxbIuWwvOaXpeWIqeS6miIsIuWwvOaXpeWIqeS6miIsMSwiIiwiIl0sWyLnur3ln4MiLCLnur3ln4MiLDEsIiIsIiJdLFsi5oyq5aiBIiwi5oyq5aiBIiwxLCIiLCIiXSxbIuivuuemj+WFi+WymyIsIuivuuemj+WFi+WymyIsMSwiIiwiIl0sWyLluJXlirMiLCLluJXlirMiLDEsIiIsIiJdLFsi55qu54m55Yev5oGp576k5bKbIiwi55qu54m55Yev5oGp576k5bKbIiwxLCIiLCIiXSxbIuiRoeiQhOeJmSIsIuiRoeiQhOeJmSIsMSwiIiwiIl0sWyLml6XmnKwiLCLml6XmnKwiLDEsIiIsIiJdLFsi55Ge5YW4Iiwi55Ge5YW4IiwxLCIiLCIiXSxbIueRnuWjqyIsIueRnuWjqyIsMSwiIiwiIl0sWyLokKjlsJTnk6blpJoiLCLokKjlsJTnk6blpJoiLDEsIiIsIiJdLFsi6JCo5pGp5LqaIiwi6JCo5pGp5LqaIiwxLCIiLCIiXSxbIuWhnuWwlOe7tOS6miIsIuWhnuWwlOe7tOS6miIsMSwiIiwiIl0sWyLloZ7mi4nliKnmmIIiLCLloZ7mi4nliKnmmIIiLDEsIiIsIiJdLFsi5aGe5YaF5Yqg5bCUIiwi5aGe5YaF5Yqg5bCUIiwxLCIiLCIiXSxbIuWhnua1pui3r+aWryIsIuWhnua1pui3r+aWryIsMSwiIiwiIl0sWyLloZ7oiIzlsJQiLCLloZ7oiIzlsJQiLDEsIiIsIiJdLFsi5rKZ54m56Zi/5ouJ5LyvIiwi5rKZ54m56Zi/5ouJ5LyvIiwxLCIiLCIiXSxbIuWco+ivnuWymyIsIuWco+ivnuWymyIsMSwiIiwiIl0sWyLlnKPlpJrnvo7lkozmma7mnpfopb/mr5QiLCLlnKPlpJrnvo7lkozmma7mnpfopb/mr5QiLDEsIiIsIiJdLFsi5Zyj6LWr5YuS5ou/Iiwi5Zyj6LWr5YuS5ou/IiwxLCIiLCIiXSxbIuWco+WfuuiMqOWSjOWwvOe7tOaWryIsIuWco+WfuuiMqOWSjOWwvOe7tOaWryIsMSwiIiwiIl0sWyLlnKPljaLopb/kupoiLCLlnKPljaLopb/kupoiLDEsIiIsIiJdLFsi5Zyj6ams5Yqb6K+6Iiwi5Zyj6ams5Yqb6K+6IiwxLCIiLCIiXSxbIuWco+aWh+ajrueJueWSjOagvOael+e6s+S4geaWryIsIuWco+aWh+ajrueJueWSjOagvOael+e6s+S4geaWryIsMSwiIiwiIl0sWyLmlq/ph4zlhbDljaEiLCLmlq/ph4zlhbDljaEiLDEsIiIsIiJdLFsi5pav5rSb5LyQ5YWLIiwi5pav5rSb5LyQ5YWLIiwxLCIiLCIiXSxbIuaWr+a0m+aWh+WwvOS6miIsIuaWr+a0m+aWh+WwvOS6miIsMSwiIiwiIl0sWyLmlq/lqIHlo6vlhbAiLCLmlq/lqIHlo6vlhbAiLDEsIiIsIiJdLFsi6IuP5Li5Iiwi6IuP5Li5IiwxLCIiLCIiXSxbIuiLj+mHjOWNlyIsIuiLj+mHjOWNlyIsMSwiIiwiIl0sWyLmiYDnvZfpl6jnvqTlspsiLCLmiYDnvZfpl6jnvqTlspsiLDEsIiIsIiJdLFsi57Si6ams6YeMIiwi57Si6ams6YeMIiwxLCIiLCIiXSxbIuWhlOWQieWFi+aWr+WdpiIsIuWhlOWQieWFi+aWr+WdpiIsMSwiIiwiIl0sWyLms7Dlm70iLCLms7Dlm70iLDEsIiIsIiJdLFsi5Z2m5qGR5bC85LqaIiwi5Z2m5qGR5bC85LqaIiwxLCIiLCIiXSxbIuaxpOWKoCIsIuaxpOWKoCIsMSwiIiwiIl0sWyLnibnnq4vlsLzovr7lkozlpJrlt7Tlk6UiLCLnibnnq4vlsLzovr7lkozlpJrlt7Tlk6UiLDEsIiIsIiJdLFsi56qB5bC85pavIiwi56qB5bC85pavIiwxLCIiLCIiXSxbIuWbvueTpuWNoiIsIuWbvueTpuWNoiIsMSwiIiwiIl0sWyLlnJ/ogLPlhbYiLCLlnJ/ogLPlhbYiLDEsIiIsIiJdLFsi5Zyf5bqT5pu85pav5Z2mIiwi5Zyf5bqT5pu85pav5Z2mIiwxLCIiLCIiXSxbIuaJmOWFi+WKsyIsIuaJmOWFi+WKsyIsMSwiIiwiIl0sWyLnk6bliKnmlq/nvqTlspvlkozlr4zlm77nurPnvqTlspsiLCLnk6bliKnmlq/nvqTlspvlkozlr4zlm77nurPnvqTlspsiLDEsIiIsIiJdLFsi55Om5Yqq6Zi/5Zu+Iiwi55Om5Yqq6Zi/5Zu+IiwxLCIiLCIiXSxbIuWNseWcsOmprOaLiSIsIuWNseWcsOmprOaLiSIsMSwiIiwiIl0sWyLlp5TlhoXnkZ7mi4kiLCLlp5TlhoXnkZ7mi4kiLDEsIiIsIiJdLFsi5paH6I6xIiwi5paH6I6xIiwxLCIiLCIiXSxbIuS5jOW5sui+viIsIuS5jOW5sui+viIsMSwiIiwiIl0sWyLkuYzlhYvlhbAiLCLkuYzlhYvlhbAiLDEsIiIsIiJdLFsi5LmM5ouJ5ZytIiwi5LmM5ouJ5ZytIiwxLCIiLCIiXSxbIuS5jOWFueWIq+WFi+aWr+WdpiIsIuS5jOWFueWIq+WFi+aWr+WdpiIsMSwiIiwiIl0sWyLopb/nj63niZkiLCLopb/nj63niZkiLDEsIiIsIiJdLFsi6KW/5pKS5ZOI5ouJIiwi6KW/5pKS5ZOI5ouJIiwxLCIiLCIiXSxbIuW4jOiFiiIsIuW4jOiFiiIsMSwiIiwiIl0sWyLmlrDliqDlnaEiLCLmlrDliqDlnaEiLDEsIiIsIiJdLFsi5paw5ZaA6YeM5aSa5bC85LqaIiwi5paw5ZaA6YeM5aSa5bC85LqaIiwxLCIiLCIiXSxbIuaWsOilv+WFsCIsIuaWsOilv+WFsCIsMSwiIiwiIl0sWyLljIjniZnliKkiLCLljIjniZnliKkiLDEsIiIsIiJdLFsi5Y+Z5Yip5LqaIiwi5Y+Z5Yip5LqaIiwxLCIiLCIiXSxbIueJmeS5sOWKoCIsIueJmeS5sOWKoCIsMSwiIiwiIl0sWyLkuprnvo7lsLzkupoiLCLkuprnvo7lsLzkupoiLDEsIiIsIiJdLFsi5Lmf6ZeoIiwi5Lmf6ZeoIiwxLCIiLCIiXSxbIuS8iuaLieWFiyIsIuS8iuaLieWFiyIsMSwiIiwiIl0sWyLkvIrmnJciLCLkvIrmnJciLDEsIiIsIiJdLFsi5Lul6Imy5YiXIiwi5Lul6Imy5YiXIiwxLCIiLCIiXSxbIuaEj+Wkp+WIqSIsIuaEj+Wkp+WIqSIsMSwiIiwiIl0sWyLljbDluqYiLCLljbDluqYiLDEsIiIsIiJdLFsi5Y2w5bqm5bC86KW/5LqaIiwi5Y2w5bqm5bC86KW/5LqaIiwxLCIiLCIiXSxbIuiLseWbvSIsIuiLseWbvSIsMSwiIiwiIl0sWyLnuqbml6YiLCLnuqbml6YiLDEsIiIsIiJdLFsi6LaK5Y2XIiwi6LaK5Y2XIiwxLCIiLCIiXSxbIui1nuavlOS6miIsIui1nuavlOS6miIsMSwiIiwiIl0sWyLms73opb/lspsiLCLms73opb/lspsiLDEsIiIsIiJdLFsi5LmN5b6XIiwi5LmN5b6XIiwxLCIiLCIiXSxbIuebtOW4g+e9l+mZgCIsIuebtOW4g+e9l+mZgCIsMSwiIiwiIl0sWyLmmbrliKkiLCLmmbrliKkiLDEsIiIsIiJdLFsi5Lit6Z2eIiwi5Lit6Z2eIiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyItMSJdfSwicDFfZGRsU2hlbmciOnsiRl9JdGVtcyI6W1siLTEiLCLpgInmi6nnnIHku70iLDEsIiIsIiJdLFsi5YyX5LqsIiwi5YyX5LqsIiwxLCIiLCIiXSxbIuWkqea0pSIsIuWkqea0pSIsMSwiIiwiIl0sWyLkuIrmtbciLCLkuIrmtbciLDEsIiIsIiJdLFsi6YeN5bqGIiwi6YeN5bqGIiwxLCIiLCIiXSxbIuays+WMlyIsIuays+WMlyIsMSwiIiwiIl0sWyLlsbHopb8iLCLlsbHopb8iLDEsIiIsIiJdLFsi6L695a6BIiwi6L695a6BIiwxLCIiLCIiXSxbIuWQieaelyIsIuWQieaelyIsMSwiIiwiIl0sWyLpu5HpvpnmsZ8iLCLpu5HpvpnmsZ8iLDEsIiIsIiJdLFsi5rGf6IuPIiwi5rGf6IuPIiwxLCIiLCIiXSxbIua1meaxnyIsIua1meaxnyIsMSwiIiwiIl0sWyLlronlvr0iLCLlronlvr0iLDEsIiIsIiJdLFsi56aP5bu6Iiwi56aP5bu6IiwxLCIiLCIiXSxbIuaxn+ilvyIsIuaxn+ilvyIsMSwiIiwiIl0sWyLlsbHkuJwiLCLlsbHkuJwiLDEsIiIsIiJdLFsi5rKz5Y2XIiwi5rKz5Y2XIiwxLCIiLCIiXSxbIua5luWMlyIsIua5luWMlyIsMSwiIiwiIl0sWyLmuZbljZciLCLmuZbljZciLDEsIiIsIiJdLFsi5bm/5LicIiwi5bm/5LicIiwxLCIiLCIiXSxbIua1t+WNlyIsIua1t+WNlyIsMSwiIiwiIl0sWyLlm5vlt50iLCLlm5vlt50iLDEsIiIsIiJdLFsi6LS15beeIiwi6LS15beeIiwxLCIiLCIiXSxbIuS6keWNlyIsIuS6keWNlyIsMSwiIiwiIl0sWyLpmZXopb8iLCLpmZXopb8iLDEsIiIsIiJdLFsi55SY6IKDIiwi55SY6IKDIiwxLCIiLCIiXSxbIumdkua1tyIsIumdkua1tyIsMSwiIiwiIl0sWyLlhoXokpnlj6QiLCLlhoXokpnlj6QiLDEsIiIsIiJdLFsi5bm/6KW/Iiwi5bm/6KW/IiwxLCIiLCIiXSxbIuilv+iXjyIsIuilv+iXjyIsMSwiIiwiIl0sWyLlroHlpI8iLCLlroHlpI8iLDEsIiIsIiJdLFsi5paw55aGIiwi5paw55aGIiwxLCIiLCIiXSxbIummmea4ryIsIummmea4ryIsMSwiIiwiIl0sWyLmvrPpl6giLCLmvrPpl6giLDEsIiIsIiJdLFsi5Y+w5rm+Iiwi5Y+w5rm+IiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyLkuIrmtbciXX0sInAxX2RkbFNoaSI6eyJFbmFibGVkIjp0cnVlLCJGX0l0ZW1zIjpbWyItMSIsIumAieaLqeW4giIsMSwiIiwiIl0sWyLkuIrmtbfluIIiLCLkuIrmtbfluIIiLDEsIiIsIiJdXSwiU2VsZWN0ZWRWYWx1ZUFycmF5IjpbIuS4iua1t+W4giJdfSwicDFfZGRsWGlhbiI6eyJFbmFibGVkIjp0cnVlLCJGX0l0ZW1zIjpbWyItMSIsIumAieaLqeWOv+WMuiIsMSwiIiwiIl0sWyLpu4TmtabljLoiLCLpu4TmtabljLoiLDEsIiIsIiJdLFsi5Y2i5rm+5Yy6Iiwi5Y2i5rm+5Yy6IiwxLCIiLCIiXSxbIuW+kOaxh+WMuiIsIuW+kOaxh+WMuiIsMSwiIiwiIl0sWyLplb/lroHljLoiLCLplb/lroHljLoiLDEsIiIsIiJdLFsi6Z2Z5a6J5Yy6Iiwi6Z2Z5a6J5Yy6IiwxLCIiLCIiXSxbIuaZrumZgOWMuiIsIuaZrumZgOWMuiIsMSwiIiwiIl0sWyLombnlj6PljLoiLCLombnlj6PljLoiLDEsIiIsIiJdLFsi5p2o5rWm5Yy6Iiwi5p2o5rWm5Yy6IiwxLCIiLCIiXSxbIuWuneWxseWMuiIsIuWuneWxseWMuiIsMSwiIiwiIl0sWyLpl7XooYzljLoiLCLpl7XooYzljLoiLDEsIiIsIiJdLFsi5ZiJ5a6a5Yy6Iiwi5ZiJ5a6a5Yy6IiwxLCIiLCIiXSxbIuadvuaxn+WMuiIsIuadvuaxn+WMuiIsMSwiIiwiIl0sWyLph5HlsbHljLoiLCLph5HlsbHljLoiLDEsIiIsIiJdLFsi6Z2S5rWm5Yy6Iiwi6Z2S5rWm5Yy6IiwxLCIiLCIiXSxbIuWliei0pOWMuiIsIuWliei0pOWMuiIsMSwiIiwiIl0sWyLmtabkuJzmlrDljLoiLCLmtabkuJzmlrDljLoiLDEsIiIsIiJdLFsi5bSH5piO5Yy6Iiwi5bSH5piO5Yy6IiwxLCIiLCIiXV0sIlNlbGVjdGVkVmFsdWVBcnJheSI6WyLmtabkuJzmlrDljLoiXX0sInAxX0ZlbmdYRFFETCI6eyJTZWxlY3RlZFZhbHVlIjoi5ZCmIiwiRl9JdGVtcyI6W1si5pivIiwi5pivIiwxXSxbIuWQpiIsIuWQpiIsMV1dfSwicDFfVG9uZ1pXRExIIjp7IlJlcXVpcmVkIjp0cnVlLCJTZWxlY3RlZFZhbHVlIjoi5ZCmIiwiRl9JdGVtcyI6W1si5pivIiwi5pivIiwxXSxbIuWQpiIsIuWQpiIsMV1dfSwicDFfWGlhbmdYRFoiOnsiTGFiZWwiOiLlm73lhoXor6bnu4blnLDlnYAiLCJUZXh0Ijoi5Yip5rSl6LevNTU15byEMTHlj7cxMDHlrqQifSwicDFfUXVlWkhaSkMiOnsiRl9JdGVtcyI6W1si5pivIiwi5pivIiwxLCIiLCIiXSxbIuWQpiIsIuWQpiIsMSwiIiwiIl1dLCJTZWxlY3RlZFZhbHVlQXJyYXkiOlsi5ZCmIl19LCJwMV9EYW5nUkdMIjp7IlNlbGVjdGVkVmFsdWUiOiLlkKYiLCJGX0l0ZW1zIjpbWyLmmK8iLCLmmK8iLDFdLFsi5ZCmIiwi5ZCmIiwxXV19LCJwMV9HZUxTTSI6eyJIaWRkZW4iOnRydWUsIklGcmFtZUF0dHJpYnV0ZXMiOnt9fSwicDFfR2VMRlMiOnsiUmVxdWlyZWQiOmZhbHNlLCJIaWRkZW4iOnRydWUsIkZfSXRlbXMiOltbIuWxheWutumalOemuyIsIuWxheWutumalOemuyIsMV0sWyLpm4bkuK3pmpTnprsiLCLpm4bkuK3pmpTnprsiLDFdXSwiU2VsZWN0ZWRWYWx1ZSI6bnVsbH0sInAxX0dlTERaIjp7IkhpZGRlbiI6dHJ1ZX0sInAxX0ZhblhSUSI6eyJIaWRkZW4iOnRydWV9LCJwMV9XZWlGSFlZIjp7IkhpZGRlbiI6dHJ1ZX0sInAxX1NoYW5nSEpaRCI6eyJIaWRkZW4iOnRydWV9LCJwMV9DZW5nRldIIjp7IkxhYmVsIjoiMjAyMOW5tDHmnIgxMOaXpeWQjuaYr+WQpuWcqOa5luWMl+mAl+eVmei/hyJ9LCJwMV9DZW5nRldIX1JpUWkiOnsiSGlkZGVuIjp0cnVlfSwicDFfQ2VuZ0ZXSF9CZWlaaHUiOnsiSGlkZGVuIjp0cnVlfSwicDFfSmllQ2h1Ijp7IkxhYmVsIjoiMDfmnIgxOOaXpeiHszA45pyIMDHml6XmmK/lkKbkuI7mnaXoh6rmuZbljJflj5Hng63kurrlkZjlr4bliIfmjqXop6YifSwicDFfSmllQ2h1X1JpUWkiOnsiSGlkZGVuIjp0cnVlfSwicDFfSmllQ2h1X0JlaVpodSI6eyJIaWRkZW4iOnRydWV9LCJwMV9UdUpXSCI6eyJMYWJlbCI6IjA35pyIMTjml6Xoh7MwOOaciDAx5pel5piv5ZCm5LmY5Z2Q5YWs5YWx5Lqk6YCa6YCU5b6E5rmW5YyXIn0sInAxX1R1SldIX1JpUWkiOnsiSGlkZGVuIjp0cnVlfSwicDFfVHVKV0hfQmVpWmh1Ijp7IkhpZGRlbiI6dHJ1ZX0sInAxX0ppYVJlbiI6eyJMYWJlbCI6IjA35pyIMTjml6Xoh7MwOOaciDAx5pel5a625Lq65piv5ZCm5pyJ5Y+R54Ot562J55eH54q2In0sInAxX0ppYVJlbl9CZWlaaHUiOnsiSGlkZGVuIjp0cnVlfSwicDFfU3VpU00iOnsiUmVxdWlyZWQiOnRydWUsIlNlbGVjdGVkVmFsdWUiOiLnu7/oibIiLCJGX0l0ZW1zIjpbWyLnuqLoibIiLCLnuqLoibIiLDFdLFsi6buE6ImyIiwi6buE6ImyIiwxXSxbIue7v+iJsiIsIue7v+iJsiIsMV1dfSwicDFfTHZNYTE0RGF5cyI6eyJSZXF1aXJlZCI6dHJ1ZSwiU2VsZWN0ZWRWYWx1ZSI6IuaYryIsIkZfSXRlbXMiOltbIuaYryIsIuaYryIsMV0sWyLlkKYiLCLlkKYiLDFdXX0sInAxX2N0bDAwX2J0blJldHVybiI6eyJPbkNsaWVudENsaWNrIjoiZG9jdW1lbnQubG9jYXRpb24uaHJlZj0nL0RlZmF1bHQuYXNweCc7cmV0dXJuOyJ9LCJwMSI6eyJJRnJhbWVBdHRyaWJ1dGVzIjp7fX19"
}


header_p_data={
    "Connection": "keep-alive",
    "Accept": "text/plain, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "X-FineUI-Ajax": "true",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://selfreport.shu.edu.cn",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

login=requests.post(url=url,headers=headers,data=userpass,allow_redirects=False)
login_first_jump=requests.get(url=r'https://newsso.shu.edu.cn/oauth/authorize?response_type=code&client_id=WUHWfrntnWYHZfzQ5QvXUCVy&redirect_uri=https%3a%2f%2fselfreport.shu.edu.cn%2fLoginSSO.aspx%3fReturnUrl%3d%252f&scope=1',headers=header_g,cookies=login.cookies,allow_redirects=False)
header_g["Sec-Fetch-Site"]="same-site"
header_g["Cache-Control"]="max-age=0"
login_second_jump=requests.get(url=login_first_jump.headers['Location'],headers=header_g,allow_redirects=False)
cookie=login_second_jump.cookies

del header_g["Sec-Fetch-User"]
del header_g["Cache-Control"]
header_g["Sec-Fetch-Site"]="none"


search_undo_report=GetUndoReport()
search_undo_report.feed(requests.get(url="https://selfreport.shu.edu.cn/ReportHistory.aspx",headers=header_g,cookies=cookie).text)

date_list=search_undo_report.date_list
print(str(datetime.date.today()))
print("\n".join(date_list)+"\n共计"+str(len(date_list))+"天")
os.system('pause')

i=0
for date in date_list:
    a=requests.get(url=r"https://selfreport.shu.edu.cn/DayReport.aspx?day="+date,headers=header_g,cookies=cookie)

    get_view_state=MyHTMLParser()
    get_view_state.feed(a.text)

    header_p_data["Referer"]="https://selfreport.shu.edu.cn/DayReport.aspx?day="+date
    data_p["p1$BaoSRQ"]=date
    data_p["__VIEWSTATE"]=get_view_state.value

    url="https://selfreport.shu.edu.cn/DayReport.aspx?day="+date
    a=requests.post(url=url,data=data_p,headers=header_p_data,cookies=cookie)
    if(a.status_code==200):
        print(date+"完成")
        i+=1
    else:
        print(date+"失败")

print("完成"+str(i)+"/"+str(len(date_list)))