import  requests

url='https://music.163.com/#/my/m/music/playlist?'

headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
}

temp='_ntes_nnid=ed27d74c036120d39b1907debcbc03ac,1619168240370; _ntes_nuid=ed27d74c036120d39b1907debcbc03ac; NMTID=00OJoXCYqKwcTZM702gnoEAfLaQnvYAAAF4_fMxLg; WM_TID=rVZMmDRaXLtAUEVBQVM6lLrj%2FkpfGjmX; ntes_kaola_ad=1; WEVNSM=1.0.0; WNMCID=kkgdxp.1623030364806.01.0; _iuqxldmzr_=32; MUSIC_U=243bb9318d87443384321461784f2654101b1cd0d5b88c15bfbd2d938bf9d7bd972cc78e2ee19b61e758fe0f42e0166243124f3fcebe94e4822778f28a0d0537; MUSIC_A_T=0; MUSIC_R_T=1414771094903; __csrf=76813e9b5c009b620d6cb876e5dca60a; JSESSIONID-WYYY=5s91IIHy7u0%5CvUTU7pe5Ua8EIuRl2WYE4w7VqK0e4vcfBpiPgCWSi0XKjVB6lhI0%2FgRy2XQyv0yRyDJXqssIlpwdaFCl5UtXCk65%5Ck1e4monZIIi36leB%2BIEcUVVuv1tRjGMAQs2B6QKZum1K%5CcVESk70bZBTe66rCd6PNiOz57KfAcN%3A1636534225328; WM_NI=suGFuJAjq1Lmq%2BUA7dxoqcq3fSm7m%2BXKDX8AlzY8HKt9Qiq6UWZ2fkme9fS5KxGX%2F5acJ5UIs0n%2F2yb%2BHY%2FvS29inXcXJLsmWSkK6NkV7RIb7nQC1t7jm4LnMIqflM%2FNcWo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed8d1658db69ed3c647f5b88ea7d84e928b9faaf533b0889ed0e179f588b885c12af0fea7c3b92ab1ab89a7f84283b6bfd2cf67b3f59ba2b670bcb1bf84f439a68da3d8f0219c958cb9bb4bb0a697d9cb41b8e79f8af43e978996d3e561afbbf787d23f89a889b9ae3fa3bd86d6d843b1f0a2d0b173a2f588baae7e91eef78aed54a18886adf267958da5acb546a98af9b3cc6af5b29fa4b480f5b6a3d5cf668f97bf87ef47ed92adb8ee37e2a3'

cookie_list=temp.split(';')
cookies={}
#for cookie in cookie_list:
#    cookies[cookie.split('=')[0]]=cookie.split('=')[-1]

cookies={cookie.split('=')[0]:cookie.split('=')[-1]for cookie in cookie_list}
data={
    'id':'309324444'
}

response=requests.get(url,headers=headers,params=data,cookies=cookies)



#start 手动设定编码格式
#response.encoding='utf8'
#打印源码str类型数据
#print(response.text)
#end

#content是存储bytes类型的响应源码，可以进行decode操作,默认utf8
#print(response.content.decode())

print(cookies)

with open('music163.html','wb')as f:
    f.write(response.content)