#!/usr/bin/env python3
import json, datetime, pathlib, urllib.request
url='https://vrchat.com/api/1/config'
req=urllib.request.Request(url,headers={'User-Agent':'VRChat-Build-Archive/1.0 (GitHub Actions)','Accept':'application/json'})
with urllib.request.urlopen(req,timeout=25) as response:
    data=json.load(response)
minimum=data['minSupportedClientBuildNumber']['PC']['minBuildNumber']
if type(minimum) is not int or not 100 <= minimum <= 100000:
    raise ValueError('Unexpected PC minimum build: '+repr(minimum))
result={'minBuildNumber':minimum,'updatedAt':datetime.datetime.now(datetime.timezone.utc).isoformat().replace('+00:00','Z'),'source':url,'field':'minSupportedClientBuildNumber.PC.minBuildNumber'}
pathlib.Path(__file__).with_name('minimum-build.json').write_text(json.dumps(result,indent=2)+'\n')
print('PC minimum supported build:',minimum)
