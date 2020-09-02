{"filter":false,"title":"extract_medical_entities.py","tooltip":"/AppointmentConcierge/ExtractMedicalEntities/extract_medical_entities.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":51,"column":12},"end":{"row":51,"column":13},"action":"insert","lines":[" "],"id":5443}],[{"start":{"row":51,"column":13},"end":{"row":51,"column":102},"action":"insert","lines":["comprehend_response['message transcript file url'].split('/')[-1].split('.')[0] + '.html'"],"id":5444}],[{"start":{"row":51,"column":97},"end":{"row":51,"column":101},"action":"remove","lines":["html"],"id":5445},{"start":{"row":51,"column":97},"end":{"row":51,"column":98},"action":"insert","lines":["j"]},{"start":{"row":51,"column":98},"end":{"row":51,"column":99},"action":"insert","lines":["s"]},{"start":{"row":51,"column":99},"end":{"row":51,"column":100},"action":"insert","lines":["o"]},{"start":{"row":51,"column":100},"end":{"row":51,"column":101},"action":"insert","lines":["n"]}],[{"start":{"row":55,"column":17},"end":{"row":55,"column":107},"action":"remove","lines":["comprehend_response['message transcript file url'].split('/')[-1].split('.')[0] + '.html')"],"id":5446},{"start":{"row":55,"column":17},"end":{"row":55,"column":26},"action":"insert","lines":["file_name"]}],[{"start":{"row":55,"column":26},"end":{"row":55,"column":27},"action":"insert","lines":[")"],"id":5447}],[{"start":{"row":51,"column":33},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":5448},{"start":{"row":52,"column":0},"end":{"row":52,"column":2},"action":"insert","lines":["\t\t"]}],[{"start":{"row":88,"column":63},"end":{"row":89,"column":0},"action":"insert","lines":["",""],"id":5450},{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":89,"column":1},"end":{"row":104,"column":77},"action":"insert","lines":["\"\"\"","\tSave the message HTML document to S3.","\t\"\"\"","\tlogger.info('Start: saving the message HTML document to S3.')","\tbucket_name = os.environ['MSG_DOC_S3_BUCKET']","\tprefix = os.environ['MSG_DOC_S3_PREFIX']","\tfile_name = file_url.split('/')[-1].split('.')[0] + '.html'","\ts3_response = s3.put_object(","\t\tBody=bytes(msg_html_doc, 'utf-8'),","\t\tBucket=bucket_name,","\t\tKey=f'{prefix}{file_name}')","\tif s3_response['ResponseMetadata']['HTTPStatusCode'] == 200:","\t\tlogger.info('Success: message HTML document written to S3.')","\telse:","\t\tlogger.error(f'Error: database service returned HTTP status code ' \\","                     f'{s3_response[\"ResponseMetadata\"][\"HTTPStatusCode\"]}.')"],"id":5451}],[{"start":{"row":90,"column":6},"end":{"row":90,"column":23},"action":"remove","lines":["the message HTML "],"id":5452},{"start":{"row":90,"column":6},"end":{"row":90,"column":7},"action":"insert","lines":["d"]},{"start":{"row":90,"column":7},"end":{"row":90,"column":8},"action":"insert","lines":["i"]},{"start":{"row":90,"column":8},"end":{"row":90,"column":9},"action":"insert","lines":["c"]},{"start":{"row":90,"column":9},"end":{"row":90,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":90,"column":10},"end":{"row":90,"column":11},"action":"insert","lines":[" "],"id":5453},{"start":{"row":90,"column":11},"end":{"row":90,"column":12},"action":"insert","lines":["o"]},{"start":{"row":90,"column":12},"end":{"row":90,"column":13},"action":"insert","lines":["b"]},{"start":{"row":90,"column":13},"end":{"row":90,"column":14},"action":"insert","lines":["j"]},{"start":{"row":90,"column":14},"end":{"row":90,"column":15},"action":"insert","lines":["e"]},{"start":{"row":90,"column":15},"end":{"row":90,"column":16},"action":"insert","lines":["c"]},{"start":{"row":90,"column":16},"end":{"row":90,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":90,"column":17},"end":{"row":90,"column":18},"action":"insert","lines":[" "],"id":5454}],[{"start":{"row":90,"column":10},"end":{"row":90,"column":11},"action":"insert","lines":["i"],"id":5455},{"start":{"row":90,"column":11},"end":{"row":90,"column":12},"action":"insert","lines":["o"]},{"start":{"row":90,"column":12},"end":{"row":90,"column":13},"action":"insert","lines":["n"]},{"start":{"row":90,"column":13},"end":{"row":90,"column":14},"action":"insert","lines":["a"]},{"start":{"row":90,"column":14},"end":{"row":90,"column":15},"action":"insert","lines":["r"]},{"start":{"row":90,"column":15},"end":{"row":90,"column":16},"action":"insert","lines":["y"]}],[{"start":{"row":90,"column":24},"end":{"row":90,"column":25},"action":"insert","lines":["a"],"id":5456},{"start":{"row":90,"column":25},"end":{"row":90,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":90,"column":26},"end":{"row":90,"column":27},"action":"insert","lines":[" "],"id":5457},{"start":{"row":90,"column":27},"end":{"row":90,"column":28},"action":"insert","lines":["J"]},{"start":{"row":90,"column":28},"end":{"row":90,"column":29},"action":"insert","lines":["S"]},{"start":{"row":90,"column":29},"end":{"row":90,"column":30},"action":"insert","lines":["O"]},{"start":{"row":90,"column":30},"end":{"row":90,"column":31},"action":"insert","lines":["N"]}],[{"start":{"row":90,"column":31},"end":{"row":90,"column":32},"action":"insert","lines":[" "],"id":5458}],[{"start":{"row":90,"column":41},"end":{"row":90,"column":43},"action":"remove","lines":["to"],"id":5459},{"start":{"row":90,"column":41},"end":{"row":90,"column":42},"action":"insert","lines":["i"]},{"start":{"row":90,"column":42},"end":{"row":90,"column":43},"action":"insert","lines":["n"]}],[{"start":{"row":92,"column":32},"end":{"row":92,"column":39},"action":"remove","lines":["message"],"id":5460},{"start":{"row":92,"column":32},"end":{"row":92,"column":33},"action":"insert","lines":["c"]},{"start":{"row":92,"column":33},"end":{"row":92,"column":34},"action":"insert","lines":["o"]},{"start":{"row":92,"column":34},"end":{"row":92,"column":35},"action":"insert","lines":["m"]},{"start":{"row":92,"column":35},"end":{"row":92,"column":36},"action":"insert","lines":["p"]},{"start":{"row":92,"column":36},"end":{"row":92,"column":37},"action":"insert","lines":["r"]},{"start":{"row":92,"column":37},"end":{"row":92,"column":38},"action":"insert","lines":["e"]},{"start":{"row":92,"column":38},"end":{"row":92,"column":39},"action":"insert","lines":["h"]},{"start":{"row":92,"column":39},"end":{"row":92,"column":40},"action":"insert","lines":["e"]},{"start":{"row":92,"column":40},"end":{"row":92,"column":41},"action":"insert","lines":["n"]},{"start":{"row":92,"column":41},"end":{"row":92,"column":42},"action":"insert","lines":["d"]}],[{"start":{"row":92,"column":42},"end":{"row":92,"column":43},"action":"insert","lines":[" "],"id":5461}],[{"start":{"row":92,"column":32},"end":{"row":92,"column":33},"action":"remove","lines":["c"],"id":5462},{"start":{"row":92,"column":32},"end":{"row":92,"column":33},"action":"insert","lines":["C"]}],[{"start":{"row":92,"column":43},"end":{"row":92,"column":44},"action":"insert","lines":["M"],"id":5463},{"start":{"row":92,"column":44},"end":{"row":92,"column":45},"action":"insert","lines":["e"]},{"start":{"row":92,"column":45},"end":{"row":92,"column":46},"action":"insert","lines":["d"]},{"start":{"row":92,"column":46},"end":{"row":92,"column":47},"action":"insert","lines":["i"]},{"start":{"row":92,"column":47},"end":{"row":92,"column":48},"action":"insert","lines":["c"]},{"start":{"row":92,"column":48},"end":{"row":92,"column":49},"action":"insert","lines":["a"]},{"start":{"row":92,"column":49},"end":{"row":92,"column":50},"action":"insert","lines":["l"]}],[{"start":{"row":92,"column":51},"end":{"row":92,"column":55},"action":"remove","lines":["HTML"],"id":5464},{"start":{"row":92,"column":51},"end":{"row":92,"column":52},"action":"insert","lines":["J"]},{"start":{"row":92,"column":52},"end":{"row":92,"column":53},"action":"insert","lines":["S"]},{"start":{"row":92,"column":53},"end":{"row":92,"column":54},"action":"insert","lines":["O"]},{"start":{"row":92,"column":54},"end":{"row":92,"column":55},"action":"insert","lines":["N"]}],[{"start":{"row":92,"column":51},"end":{"row":92,"column":52},"action":"insert","lines":["r"],"id":5465},{"start":{"row":92,"column":52},"end":{"row":92,"column":53},"action":"insert","lines":["e"]},{"start":{"row":92,"column":53},"end":{"row":92,"column":54},"action":"insert","lines":["s"]},{"start":{"row":92,"column":54},"end":{"row":92,"column":55},"action":"insert","lines":["u"]},{"start":{"row":92,"column":55},"end":{"row":92,"column":56},"action":"insert","lines":["l"]},{"start":{"row":92,"column":56},"end":{"row":92,"column":57},"action":"insert","lines":["t"]},{"start":{"row":92,"column":57},"end":{"row":92,"column":58},"action":"insert","lines":["s"]}],[{"start":{"row":92,"column":58},"end":{"row":92,"column":59},"action":"insert","lines":[" "],"id":5466}],[{"start":{"row":92,"column":59},"end":{"row":92,"column":72},"action":"remove","lines":["JSON document"],"id":5467},{"start":{"row":92,"column":59},"end":{"row":92,"column":60},"action":"remove","lines":[" "]}],[{"start":{"row":88,"column":30},"end":{"row":88,"column":33},"action":"remove","lines":["s3_"],"id":5468}],[{"start":{"row":88,"column":36},"end":{"row":88,"column":37},"action":"insert","lines":["_"],"id":5469},{"start":{"row":88,"column":37},"end":{"row":88,"column":38},"action":"insert","lines":["n"]},{"start":{"row":88,"column":38},"end":{"row":88,"column":39},"action":"insert","lines":["a"]},{"start":{"row":88,"column":39},"end":{"row":88,"column":40},"action":"insert","lines":["m"]},{"start":{"row":88,"column":40},"end":{"row":88,"column":41},"action":"insert","lines":["e"]}],[{"start":{"row":88,"column":43},"end":{"row":88,"column":44},"action":"remove","lines":["s"],"id":5470},{"start":{"row":88,"column":43},"end":{"row":88,"column":44},"action":"remove","lines":["3"]},{"start":{"row":88,"column":43},"end":{"row":88,"column":44},"action":"remove","lines":["_"]}],[{"start":{"row":93,"column":0},"end":{"row":96,"column":0},"action":"remove","lines":["\tbucket_name = os.environ['MSG_DOC_S3_BUCKET']","\tprefix = os.environ['MSG_DOC_S3_PREFIX']","\tfile_name = file_url.split('/')[-1].split('.')[0] + '.html'",""],"id":5471}],[{"start":{"row":94,"column":13},"end":{"row":94,"column":25},"action":"remove","lines":["msg_html_doc"],"id":5472},{"start":{"row":94,"column":13},"end":{"row":94,"column":23},"action":"insert","lines":["json.dumps"]}],[{"start":{"row":94,"column":23},"end":{"row":94,"column":24},"action":"insert","lines":["("],"id":5473},{"start":{"row":94,"column":24},"end":{"row":94,"column":25},"action":"insert","lines":[")"]}],[{"start":{"row":94,"column":24},"end":{"row":94,"column":32},"action":"insert","lines":["dict_obj"],"id":5474}],[{"start":{"row":98,"column":24},"end":{"row":98,"column":60},"action":"remove","lines":["message HTML document written to S3."],"id":5475},{"start":{"row":98,"column":24},"end":{"row":98,"column":68},"action":"insert","lines":["saving the Comprehend Medical results to S3."]}],[{"start":{"row":98,"column":24},"end":{"row":98,"column":35},"action":"remove","lines":["saving the "],"id":5476}],[{"start":{"row":98,"column":51},"end":{"row":98,"column":52},"action":"insert","lines":["s"],"id":5477},{"start":{"row":98,"column":52},"end":{"row":98,"column":53},"action":"insert","lines":["a"]},{"start":{"row":98,"column":53},"end":{"row":98,"column":54},"action":"insert","lines":["v"]},{"start":{"row":98,"column":54},"end":{"row":98,"column":55},"action":"insert","lines":["e"]},{"start":{"row":98,"column":55},"end":{"row":98,"column":56},"action":"insert","lines":["d"]}],[{"start":{"row":98,"column":56},"end":{"row":98,"column":57},"action":"insert","lines":[" "],"id":5478}],[{"start":{"row":100,"column":24},"end":{"row":100,"column":32},"action":"remove","lines":["database"],"id":5479},{"start":{"row":100,"column":24},"end":{"row":100,"column":25},"action":"insert","lines":["S"]},{"start":{"row":100,"column":25},"end":{"row":100,"column":26},"action":"insert","lines":["3"]}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":1},"action":"remove","lines":["\t"],"id":5480},{"start":{"row":103,"column":0},"end":{"row":104,"column":1},"action":"remove","lines":["","\t"]}],[{"start":{"row":103,"column":0},"end":{"row":104,"column":0},"action":"remove","lines":["",""],"id":5481}],[{"start":{"row":94,"column":32},"end":{"row":94,"column":33},"action":"insert","lines":[","],"id":5482}],[{"start":{"row":94,"column":33},"end":{"row":94,"column":34},"action":"insert","lines":[" "],"id":5483}],[{"start":{"row":94,"column":34},"end":{"row":94,"column":45},"action":"insert","lines":["default=str"],"id":5484}],[{"start":{"row":80,"column":63},"end":{"row":81,"column":0},"action":"insert","lines":["",""],"id":5485},{"start":{"row":81,"column":0},"end":{"row":81,"column":2},"action":"insert","lines":["\t\t"]}],[{"start":{"row":81,"column":2},"end":{"row":81,"column":63},"action":"insert","lines":["comprehend_response['message transcript file url'] = file_url"],"id":5486}],[{"start":{"row":81,"column":31},"end":{"row":81,"column":50},"action":"remove","lines":["transcript file url"],"id":5487},{"start":{"row":81,"column":31},"end":{"row":81,"column":32},"action":"insert","lines":["I"]},{"start":{"row":81,"column":32},"end":{"row":81,"column":33},"action":"insert","lines":["D"]}],[{"start":{"row":81,"column":0},"end":{"row":81,"column":46},"action":"remove","lines":["\t\tcomprehend_response['message ID'] = file_url"],"id":5488},{"start":{"row":81,"column":0},"end":{"row":82,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":78,"column":62},"end":{"row":79,"column":0},"action":"insert","lines":["",""],"id":5489},{"start":{"row":79,"column":0},"end":{"row":79,"column":2},"action":"insert","lines":["\t\t"]}],[{"start":{"row":79,"column":2},"end":{"row":79,"column":48},"action":"insert","lines":["\t\tcomprehend_response['message ID'] = file_url"],"id":5490}],[{"start":{"row":79,"column":3},"end":{"row":79,"column":4},"action":"remove","lines":["\t"],"id":5491},{"start":{"row":79,"column":2},"end":{"row":79,"column":3},"action":"remove","lines":["\t"]},{"start":{"row":79,"column":1},"end":{"row":79,"column":2},"action":"remove","lines":["\t"]}],[{"start":{"row":79,"column":1},"end":{"row":79,"column":2},"action":"insert","lines":["\t"],"id":5492}],[{"start":{"row":79,"column":46},"end":{"row":79,"column":47},"action":"insert","lines":["."],"id":5493},{"start":{"row":79,"column":47},"end":{"row":79,"column":48},"action":"insert","lines":["s"]},{"start":{"row":79,"column":48},"end":{"row":79,"column":49},"action":"insert","lines":["p"]},{"start":{"row":79,"column":49},"end":{"row":79,"column":50},"action":"insert","lines":["l"]},{"start":{"row":79,"column":50},"end":{"row":79,"column":51},"action":"insert","lines":["i"]},{"start":{"row":79,"column":51},"end":{"row":79,"column":52},"action":"insert","lines":["t"]}],[{"start":{"row":79,"column":52},"end":{"row":79,"column":54},"action":"insert","lines":["()"],"id":5494}],[{"start":{"row":79,"column":52},"end":{"row":79,"column":54},"action":"remove","lines":["()"],"id":5495}],[{"start":{"row":79,"column":52},"end":{"row":79,"column":54},"action":"insert","lines":["[]"],"id":5496}],[{"start":{"row":79,"column":52},"end":{"row":79,"column":54},"action":"remove","lines":["[]"],"id":5497}],[{"start":{"row":79,"column":52},"end":{"row":79,"column":54},"action":"insert","lines":["()"],"id":5498}],[{"start":{"row":79,"column":53},"end":{"row":79,"column":55},"action":"insert","lines":["''"],"id":5499}],[{"start":{"row":79,"column":54},"end":{"row":79,"column":55},"action":"insert","lines":["/"],"id":5500}],[{"start":{"row":79,"column":57},"end":{"row":79,"column":59},"action":"insert","lines":["[]"],"id":5501}],[{"start":{"row":79,"column":58},"end":{"row":79,"column":59},"action":"insert","lines":["-"],"id":5502},{"start":{"row":79,"column":59},"end":{"row":79,"column":60},"action":"insert","lines":["1"]}],[{"start":{"row":79,"column":61},"end":{"row":79,"column":62},"action":"insert","lines":["."],"id":5503},{"start":{"row":79,"column":62},"end":{"row":79,"column":63},"action":"insert","lines":["s"]},{"start":{"row":79,"column":63},"end":{"row":79,"column":64},"action":"insert","lines":["p"]},{"start":{"row":79,"column":64},"end":{"row":79,"column":65},"action":"insert","lines":["l"]},{"start":{"row":79,"column":65},"end":{"row":79,"column":66},"action":"insert","lines":["i"]},{"start":{"row":79,"column":66},"end":{"row":79,"column":67},"action":"insert","lines":["t"]}],[{"start":{"row":79,"column":67},"end":{"row":79,"column":69},"action":"insert","lines":["()"],"id":5504}],[{"start":{"row":79,"column":68},"end":{"row":79,"column":70},"action":"insert","lines":["''"],"id":5505}],[{"start":{"row":79,"column":69},"end":{"row":79,"column":70},"action":"insert","lines":["."],"id":5506}],[{"start":{"row":79,"column":72},"end":{"row":79,"column":74},"action":"insert","lines":["[]"],"id":5507}],[{"start":{"row":79,"column":73},"end":{"row":79,"column":74},"action":"insert","lines":["0"],"id":5508}],[{"start":{"row":78,"column":30},"end":{"row":78,"column":32},"action":"remove","lines":[" t"],"id":5509},{"start":{"row":78,"column":30},"end":{"row":78,"column":31},"action":"insert","lines":["T"]}],[{"start":{"row":79,"column":30},"end":{"row":79,"column":31},"action":"remove","lines":[" "],"id":5510}],[{"start":{"row":79,"column":31},"end":{"row":79,"column":32},"action":"remove","lines":["D"],"id":5511},{"start":{"row":79,"column":31},"end":{"row":79,"column":32},"action":"insert","lines":["d"]}],[{"start":{"row":80,"column":30},"end":{"row":80,"column":32},"action":"remove","lines":[" t"],"id":5512},{"start":{"row":80,"column":30},"end":{"row":80,"column":31},"action":"insert","lines":["T"]}],[{"start":{"row":80,"column":40},"end":{"row":80,"column":42},"action":"remove","lines":[" t"],"id":5513},{"start":{"row":80,"column":40},"end":{"row":80,"column":41},"action":"insert","lines":["T"]}],[{"start":{"row":81,"column":30},"end":{"row":81,"column":32},"action":"remove","lines":[" t"],"id":5514},{"start":{"row":81,"column":30},"end":{"row":81,"column":31},"action":"insert","lines":["T"]}],[{"start":{"row":81,"column":40},"end":{"row":81,"column":42},"action":"remove","lines":[" f"],"id":5515},{"start":{"row":81,"column":40},"end":{"row":81,"column":41},"action":"insert","lines":["F"]}],[{"start":{"row":81,"column":44},"end":{"row":81,"column":46},"action":"remove","lines":[" u"],"id":5516},{"start":{"row":81,"column":44},"end":{"row":81,"column":45},"action":"insert","lines":["U"]}],[{"start":{"row":78,"column":61},"end":{"row":78,"column":62},"action":"insert","lines":[" "],"id":5517}],[{"start":{"row":78,"column":62},"end":{"row":78,"column":148},"action":"insert","lines":["msg_data[\"message time\"] + datetime.timedelta(hours=4)).strftime(\"%B %d, %Y %H:%M:%S\")"],"id":5518}],[{"start":{"row":78,"column":62},"end":{"row":78,"column":86},"action":"remove","lines":["msg_data[\"message time\"]"],"id":5519},{"start":{"row":78,"column":62},"end":{"row":78,"column":63},"action":"remove","lines":[" "]}],[{"start":{"row":78,"column":102},"end":{"row":78,"column":103},"action":"remove","lines":["\""],"id":5520},{"start":{"row":78,"column":102},"end":{"row":78,"column":103},"action":"insert","lines":["'"]}],[{"start":{"row":78,"column":121},"end":{"row":78,"column":122},"action":"remove","lines":["\""],"id":5521},{"start":{"row":78,"column":121},"end":{"row":78,"column":122},"action":"insert","lines":["'"]}],[{"start":{"row":78,"column":102},"end":{"row":78,"column":122},"action":"remove","lines":["'%B %d, %Y %H:%M:%S'"],"id":5522},{"start":{"row":78,"column":102},"end":{"row":78,"column":121},"action":"insert","lines":["'%Y-%M-%d %H:%M:%S'"]}],[{"start":{"row":78,"column":39},"end":{"row":78,"column":40},"action":"insert","lines":["("],"id":5523}],[{"start":{"row":60,"column":47},"end":{"row":60,"column":74},"action":"remove","lines":["message transcript file url"],"id":5524},{"start":{"row":60,"column":47},"end":{"row":60,"column":71},"action":"insert","lines":["messageTranscriptFileUrl"]}],[{"start":{"row":52,"column":3},"end":{"row":52,"column":30},"action":"remove","lines":["message transcript file url"],"id":5525},{"start":{"row":52,"column":3},"end":{"row":52,"column":27},"action":"insert","lines":["messageTranscriptFileUrl"]}],[{"start":{"row":78,"column":30},"end":{"row":78,"column":31},"action":"insert","lines":[" "],"id":5526}],[{"start":{"row":137,"column":46},"end":{"row":137,"column":48},"action":"remove","lines":[" t"],"id":5527},{"start":{"row":137,"column":46},"end":{"row":137,"column":47},"action":"insert","lines":["T"]}],[{"start":{"row":138,"column":57},"end":{"row":138,"column":59},"action":"remove","lines":[" t"],"id":5528},{"start":{"row":138,"column":57},"end":{"row":138,"column":58},"action":"insert","lines":["T"]}],[{"start":{"row":138,"column":67},"end":{"row":138,"column":69},"action":"remove","lines":[" t"],"id":5529},{"start":{"row":138,"column":67},"end":{"row":138,"column":68},"action":"insert","lines":["T"]}],[{"start":{"row":78,"column":30},"end":{"row":78,"column":31},"action":"remove","lines":[" "],"id":5530}],[{"start":{"row":191,"column":93},"end":{"row":191,"column":94},"action":"insert","lines":["."],"id":5531},{"start":{"row":191,"column":94},"end":{"row":191,"column":95},"action":"insert","lines":["%"]},{"start":{"row":191,"column":95},"end":{"row":191,"column":96},"action":"insert","lines":["f"]}],[{"start":{"row":191,"column":93},"end":{"row":191,"column":96},"action":"remove","lines":[".%f"],"id":5532}],[{"start":{"row":78,"column":121},"end":{"row":78,"column":124},"action":"insert","lines":[".%f"],"id":5533}],[{"start":{"row":191,"column":101},"end":{"row":192,"column":0},"action":"insert","lines":["",""],"id":5534},{"start":{"row":192,"column":0},"end":{"row":192,"column":5},"action":"insert","lines":["\t\t\t\t\t"]},{"start":{"row":192,"column":5},"end":{"row":193,"column":0},"action":"insert","lines":["",""]},{"start":{"row":193,"column":0},"end":{"row":193,"column":5},"action":"insert","lines":["\t\t\t\t\t"]},{"start":{"row":193,"column":5},"end":{"row":194,"column":0},"action":"insert","lines":["",""]},{"start":{"row":194,"column":0},"end":{"row":194,"column":5},"action":"insert","lines":["\t\t\t\t\t"]},{"start":{"row":194,"column":5},"end":{"row":195,"column":0},"action":"insert","lines":["",""]},{"start":{"row":195,"column":0},"end":{"row":195,"column":5},"action":"insert","lines":["\t\t\t\t\t"]}],[{"start":{"row":195,"column":4},"end":{"row":195,"column":5},"action":"remove","lines":["\t"],"id":5535},{"start":{"row":195,"column":3},"end":{"row":195,"column":4},"action":"remove","lines":["\t"]},{"start":{"row":195,"column":2},"end":{"row":195,"column":3},"action":"remove","lines":["\t"]},{"start":{"row":195,"column":1},"end":{"row":195,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":195,"column":0},"end":{"row":195,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":194,"column":5},"end":{"row":195,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":193,"column":0},"end":{"row":195,"column":0},"action":"insert","lines":["\tmsg_html_doc += f'<p><b>Message Received : </b>' \\","\t\t\t\t\tf'{(msg_data[\"message time\"] + datetime.timedelta(hours=4)).strftime(\"%B %d, %Y %H:%M:%S\")}</p>'",""],"id":5536}],[{"start":{"row":195,"column":0},"end":{"row":197,"column":0},"action":"remove","lines":["\t\t\t\t\t","\t\t\t\t\t",""],"id":5537}],[{"start":{"row":193,"column":1},"end":{"row":193,"column":3},"action":"insert","lines":["# "],"id":5538},{"start":{"row":194,"column":1},"end":{"row":194,"column":3},"action":"insert","lines":["# "]}],[{"start":{"row":192,"column":0},"end":{"row":193,"column":0},"action":"remove","lines":["\t\t\t\t\t",""],"id":5539}],[{"start":{"row":191,"column":8},"end":{"row":191,"column":9},"action":"remove","lines":["("],"id":5540}],[{"start":{"row":191,"column":32},"end":{"row":191,"column":94},"action":"remove","lines":[" + datetime.timedelta(hours=4)).strftime(\"%B %d, %Y %H:%M:%S\")"],"id":5541}],[{"start":{"row":78,"column":108},"end":{"row":78,"column":109},"action":"remove","lines":["M"],"id":5542},{"start":{"row":78,"column":108},"end":{"row":78,"column":109},"action":"insert","lines":["m"]}],[{"start":{"row":78,"column":123},"end":{"row":78,"column":124},"action":"remove","lines":["f"],"id":5543},{"start":{"row":78,"column":122},"end":{"row":78,"column":123},"action":"remove","lines":["%"]},{"start":{"row":78,"column":121},"end":{"row":78,"column":122},"action":"remove","lines":["."]}],[{"start":{"row":192,"column":0},"end":{"row":194,"column":0},"action":"remove","lines":["\t# msg_html_doc += f'<p><b>Message Received : </b>' \\","\t# \t\t\t\tf'{(msg_data[\"message time\"] + datetime.timedelta(hours=4)).strftime(\"%B %d, %Y %H:%M:%S\")}</p>'",""],"id":5544}]]},"ace":{"folds":[],"scrolltop":1095,"scrollleft":0,"selection":{"start":{"row":76,"column":34},"end":{"row":76,"column":52},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":53,"state":"start","mode":"ace/mode/python"}},"timestamp":1599031214667,"hash":"adf81ddaff3c3511b53f26ad4fa0c677206291b0"}