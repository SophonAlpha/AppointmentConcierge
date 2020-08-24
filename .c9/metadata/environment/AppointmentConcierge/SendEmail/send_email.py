{"filter":false,"title":"send_email.py","tooltip":"/AppointmentConcierge/SendEmail/send_email.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":8,"column":0},"end":{"row":8,"column":46},"action":"insert","lines":["from email.mime.multipart import MIMEMultipart"],"id":394}],[{"start":{"row":92,"column":4},"end":{"row":95,"column":30},"action":"insert","lines":["message = MIMEMultipart(\"alternative\")","message[\"Subject\"] = \"multipart test\"","message[\"From\"] = sender_email","message[\"To\"] = receiver_email"],"id":395}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "],"id":396}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"insert","lines":["    "],"id":397}],[{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"insert","lines":["    "],"id":398}],[{"start":{"row":94,"column":22},"end":{"row":94,"column":34},"action":"remove","lines":["sender_email"],"id":399},{"start":{"row":94,"column":22},"end":{"row":94,"column":28},"action":"insert","lines":["config"]}],[{"start":{"row":94,"column":28},"end":{"row":94,"column":30},"action":"insert","lines":["[]"],"id":400}],[{"start":{"row":94,"column":29},"end":{"row":94,"column":31},"action":"insert","lines":["''"],"id":401}],[{"start":{"row":94,"column":30},"end":{"row":94,"column":31},"action":"insert","lines":["S"],"id":402},{"start":{"row":94,"column":31},"end":{"row":94,"column":32},"action":"insert","lines":["e"]},{"start":{"row":94,"column":32},"end":{"row":94,"column":33},"action":"insert","lines":["n"]},{"start":{"row":94,"column":33},"end":{"row":94,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":94,"column":30},"end":{"row":94,"column":34},"action":"remove","lines":["Send"],"id":403},{"start":{"row":94,"column":30},"end":{"row":94,"column":39},"action":"insert","lines":["SendEmail"]}],[{"start":{"row":94,"column":41},"end":{"row":94,"column":43},"action":"insert","lines":["[]"],"id":404}],[{"start":{"row":94,"column":42},"end":{"row":94,"column":61},"action":"insert","lines":["'smtp-sender-email'"],"id":405}],[{"start":{"row":95,"column":20},"end":{"row":95,"column":34},"action":"remove","lines":["receiver_email"],"id":406},{"start":{"row":95,"column":20},"end":{"row":95,"column":60},"action":"insert","lines":["config['SendEmail']['smtp-sender-email']"]}],[{"start":{"row":92,"column":28},"end":{"row":92,"column":41},"action":"remove","lines":["\"alternative\""],"id":407}],[{"start":{"row":93,"column":26},"end":{"row":93,"column":40},"action":"remove","lines":["multipart test"],"id":408},{"start":{"row":93,"column":26},"end":{"row":93,"column":27},"action":"insert","lines":["["]},{"start":{"row":93,"column":27},"end":{"row":93,"column":28},"action":"insert","lines":["A"]},{"start":{"row":93,"column":28},"end":{"row":93,"column":29},"action":"insert","lines":["p"]},{"start":{"row":93,"column":29},"end":{"row":93,"column":30},"action":"insert","lines":["p"]},{"start":{"row":93,"column":30},"end":{"row":93,"column":31},"action":"insert","lines":["o"]},{"start":{"row":93,"column":31},"end":{"row":93,"column":32},"action":"insert","lines":["i"]}],[{"start":{"row":93,"column":32},"end":{"row":93,"column":33},"action":"insert","lines":["n"],"id":409},{"start":{"row":93,"column":33},"end":{"row":93,"column":34},"action":"insert","lines":["t"]},{"start":{"row":93,"column":34},"end":{"row":93,"column":35},"action":"insert","lines":["n"]},{"start":{"row":93,"column":35},"end":{"row":93,"column":36},"action":"insert","lines":["e"]}],[{"start":{"row":93,"column":35},"end":{"row":93,"column":36},"action":"remove","lines":["e"],"id":410},{"start":{"row":93,"column":34},"end":{"row":93,"column":35},"action":"remove","lines":["n"]}],[{"start":{"row":93,"column":34},"end":{"row":93,"column":35},"action":"insert","lines":["m"],"id":411},{"start":{"row":93,"column":35},"end":{"row":93,"column":36},"action":"insert","lines":["e"]},{"start":{"row":93,"column":36},"end":{"row":93,"column":37},"action":"insert","lines":["n"]},{"start":{"row":93,"column":37},"end":{"row":93,"column":38},"action":"insert","lines":["t"]}],[{"start":{"row":93,"column":38},"end":{"row":93,"column":39},"action":"insert","lines":[" "],"id":412},{"start":{"row":93,"column":39},"end":{"row":93,"column":40},"action":"insert","lines":["C"]},{"start":{"row":93,"column":40},"end":{"row":93,"column":41},"action":"insert","lines":["o"]},{"start":{"row":93,"column":41},"end":{"row":93,"column":42},"action":"insert","lines":["n"]},{"start":{"row":93,"column":42},"end":{"row":93,"column":43},"action":"insert","lines":["c"]},{"start":{"row":93,"column":43},"end":{"row":93,"column":44},"action":"insert","lines":["i"]},{"start":{"row":93,"column":44},"end":{"row":93,"column":45},"action":"insert","lines":["e"]}],[{"start":{"row":93,"column":45},"end":{"row":93,"column":46},"action":"insert","lines":["r"],"id":413},{"start":{"row":93,"column":46},"end":{"row":93,"column":47},"action":"insert","lines":["g"]},{"start":{"row":93,"column":47},"end":{"row":93,"column":48},"action":"insert","lines":["e"]},{"start":{"row":93,"column":48},"end":{"row":93,"column":49},"action":"insert","lines":["]"]}],[{"start":{"row":93,"column":49},"end":{"row":93,"column":50},"action":"insert","lines":[" "],"id":414},{"start":{"row":93,"column":50},"end":{"row":93,"column":51},"action":"insert","lines":["-"]}],[{"start":{"row":93,"column":51},"end":{"row":93,"column":52},"action":"insert","lines":[" "],"id":415}],[{"start":{"row":93,"column":52},"end":{"row":93,"column":53},"action":"insert","lines":["v"],"id":416},{"start":{"row":93,"column":53},"end":{"row":93,"column":54},"action":"insert","lines":["o"]},{"start":{"row":93,"column":54},"end":{"row":93,"column":55},"action":"insert","lines":["i"]},{"start":{"row":93,"column":55},"end":{"row":93,"column":56},"action":"insert","lines":["c"]},{"start":{"row":93,"column":56},"end":{"row":93,"column":57},"action":"insert","lines":["e"]}],[{"start":{"row":93,"column":57},"end":{"row":93,"column":58},"action":"insert","lines":[" "],"id":417},{"start":{"row":93,"column":58},"end":{"row":93,"column":59},"action":"insert","lines":["m"]},{"start":{"row":93,"column":59},"end":{"row":93,"column":60},"action":"insert","lines":["e"]},{"start":{"row":93,"column":60},"end":{"row":93,"column":61},"action":"insert","lines":["s"]},{"start":{"row":93,"column":61},"end":{"row":93,"column":62},"action":"insert","lines":["s"]},{"start":{"row":93,"column":62},"end":{"row":93,"column":63},"action":"insert","lines":["a"]},{"start":{"row":93,"column":63},"end":{"row":93,"column":64},"action":"insert","lines":["g"]},{"start":{"row":93,"column":64},"end":{"row":93,"column":65},"action":"insert","lines":["e"]}],[{"start":{"row":93,"column":65},"end":{"row":93,"column":66},"action":"insert","lines":[" "],"id":418},{"start":{"row":93,"column":66},"end":{"row":93,"column":67},"action":"insert","lines":["t"]},{"start":{"row":93,"column":67},"end":{"row":93,"column":68},"action":"insert","lines":["r"]},{"start":{"row":93,"column":68},"end":{"row":93,"column":69},"action":"insert","lines":["a"]},{"start":{"row":93,"column":69},"end":{"row":93,"column":70},"action":"insert","lines":["n"]},{"start":{"row":93,"column":70},"end":{"row":93,"column":71},"action":"insert","lines":["s"]},{"start":{"row":93,"column":71},"end":{"row":93,"column":72},"action":"insert","lines":["c"]}],[{"start":{"row":93,"column":72},"end":{"row":93,"column":73},"action":"insert","lines":["r"],"id":419},{"start":{"row":93,"column":73},"end":{"row":93,"column":74},"action":"insert","lines":["i"]},{"start":{"row":93,"column":74},"end":{"row":93,"column":75},"action":"insert","lines":["p"]},{"start":{"row":93,"column":75},"end":{"row":93,"column":76},"action":"insert","lines":["t"]}],[{"start":{"row":95,"column":60},"end":{"row":96,"column":0},"action":"insert","lines":["",""],"id":420},{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":96,"column":4},"end":{"row":96,"column":42},"action":"insert","lines":["message.attach(MIMEText(html, \"html\"))"],"id":421}],[{"start":{"row":96,"column":28},"end":{"row":96,"column":32},"action":"remove","lines":["html"],"id":422},{"start":{"row":96,"column":28},"end":{"row":96,"column":35},"action":"insert","lines":["msg_doc"]}],[{"start":{"row":96,"column":45},"end":{"row":97,"column":0},"action":"insert","lines":["",""],"id":423},{"start":{"row":97,"column":0},"end":{"row":97,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":97,"column":4},"end":{"row":105,"column":0},"action":"insert","lines":["with smtplib.SMTP(smtp_server, port) as server:","    server.ehlo()","    server.starttls()","    server.ehlo()","    server.login(user_id, password)","    server.sendmail(","        sender_email, receiver_email, message.as_string()","    )",""],"id":424}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "],"id":425},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":4},"action":"insert","lines":["    "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":8},"action":"remove","lines":["        "],"id":426},{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":98,"column":4},"end":{"row":98,"column":8},"action":"insert","lines":["    "],"id":427}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":8},"action":"remove","lines":["        "],"id":428},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":99,"column":4},"end":{"row":99,"column":8},"action":"insert","lines":["    "],"id":429}],[{"start":{"row":100,"column":0},"end":{"row":100,"column":8},"action":"remove","lines":["        "],"id":430},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":100,"column":4},"end":{"row":100,"column":8},"action":"insert","lines":["    "],"id":431}],[{"start":{"row":101,"column":0},"end":{"row":101,"column":8},"action":"remove","lines":["        "],"id":432},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":101,"column":4},"end":{"row":101,"column":8},"action":"insert","lines":["    "],"id":433}],[{"start":{"row":102,"column":0},"end":{"row":102,"column":8},"action":"remove","lines":["        "],"id":434},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":102,"column":4},"end":{"row":102,"column":8},"action":"insert","lines":["    "],"id":435}],[{"start":{"row":103,"column":0},"end":{"row":103,"column":12},"action":"remove","lines":["            "],"id":436},{"start":{"row":103,"column":0},"end":{"row":103,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":103,"column":4},"end":{"row":103,"column":8},"action":"insert","lines":["    "],"id":437}],[{"start":{"row":103,"column":8},"end":{"row":103,"column":12},"action":"insert","lines":["    "],"id":438}],[{"start":{"row":97,"column":0},"end":{"row":97,"column":4},"action":"remove","lines":["    "],"id":439},{"start":{"row":97,"column":0},"end":{"row":97,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":97,"column":22},"end":{"row":97,"column":33},"action":"remove","lines":["smtp_server"],"id":440},{"start":{"row":97,"column":22},"end":{"row":97,"column":41},"action":"insert","lines":["config['SendEmail']"]}],[{"start":{"row":97,"column":41},"end":{"row":97,"column":42},"action":"insert","lines":["["],"id":441},{"start":{"row":97,"column":42},"end":{"row":97,"column":43},"action":"insert","lines":["]"]}],[{"start":{"row":97,"column":42},"end":{"row":97,"column":44},"action":"insert","lines":["''"],"id":442}],[{"start":{"row":97,"column":43},"end":{"row":97,"column":44},"action":"insert","lines":["s"],"id":443},{"start":{"row":97,"column":44},"end":{"row":97,"column":45},"action":"insert","lines":["m"]},{"start":{"row":97,"column":45},"end":{"row":97,"column":46},"action":"insert","lines":["t"]},{"start":{"row":97,"column":46},"end":{"row":97,"column":47},"action":"insert","lines":["p"]},{"start":{"row":97,"column":47},"end":{"row":97,"column":48},"action":"insert","lines":["-"]},{"start":{"row":97,"column":48},"end":{"row":97,"column":49},"action":"insert","lines":["s"]},{"start":{"row":97,"column":49},"end":{"row":97,"column":50},"action":"insert","lines":["e"]}],[{"start":{"row":97,"column":50},"end":{"row":97,"column":51},"action":"insert","lines":["r"],"id":444},{"start":{"row":97,"column":51},"end":{"row":97,"column":52},"action":"insert","lines":["v"]},{"start":{"row":97,"column":52},"end":{"row":97,"column":53},"action":"insert","lines":["e"]},{"start":{"row":97,"column":53},"end":{"row":97,"column":54},"action":"insert","lines":["r"]}],[{"start":{"row":97,"column":22},"end":{"row":98,"column":0},"action":"insert","lines":["",""],"id":445},{"start":{"row":98,"column":0},"end":{"row":98,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":98,"column":48},"end":{"row":99,"column":0},"action":"insert","lines":["",""],"id":446},{"start":{"row":99,"column":0},"end":{"row":99,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":98,"column":44},"end":{"row":98,"column":48},"action":"remove","lines":["port"],"id":447},{"start":{"row":98,"column":44},"end":{"row":98,"column":78},"action":"insert","lines":["config['SendEmail']['smtp-server']"]}],[{"start":{"row":98,"column":70},"end":{"row":98,"column":76},"action":"remove","lines":["server"],"id":448},{"start":{"row":98,"column":70},"end":{"row":98,"column":71},"action":"insert","lines":["p"]},{"start":{"row":98,"column":71},"end":{"row":98,"column":72},"action":"insert","lines":["o"]},{"start":{"row":98,"column":72},"end":{"row":98,"column":73},"action":"insert","lines":["r"]},{"start":{"row":98,"column":73},"end":{"row":98,"column":74},"action":"insert","lines":["t"]}],[{"start":{"row":103,"column":21},"end":{"row":103,"column":28},"action":"remove","lines":["user_id"],"id":449},{"start":{"row":103,"column":21},"end":{"row":103,"column":40},"action":"insert","lines":["config['SendEmail']"]}],[{"start":{"row":103,"column":40},"end":{"row":103,"column":41},"action":"insert","lines":["["],"id":450}],[{"start":{"row":103,"column":41},"end":{"row":103,"column":43},"action":"insert","lines":["''"],"id":451}],[{"start":{"row":103,"column":43},"end":{"row":103,"column":44},"action":"insert","lines":["]"],"id":452}],[{"start":{"row":103,"column":42},"end":{"row":103,"column":56},"action":"insert","lines":["'smtp-user-id'"],"id":453}],[{"start":{"row":103,"column":56},"end":{"row":103,"column":57},"action":"remove","lines":["'"],"id":454}],[{"start":{"row":103,"column":42},"end":{"row":103,"column":43},"action":"remove","lines":["'"],"id":455}],[{"start":{"row":103,"column":57},"end":{"row":103,"column":58},"action":"remove","lines":[" "],"id":456}],[{"start":{"row":103,"column":57},"end":{"row":104,"column":0},"action":"insert","lines":["",""],"id":457},{"start":{"row":104,"column":0},"end":{"row":104,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":104,"column":8},"end":{"row":104,"column":12},"action":"insert","lines":["    "],"id":458}],[{"start":{"row":104,"column":12},"end":{"row":104,"column":16},"action":"insert","lines":["    "],"id":459}],[{"start":{"row":104,"column":16},"end":{"row":104,"column":20},"action":"insert","lines":["    "],"id":460}],[{"start":{"row":104,"column":20},"end":{"row":104,"column":28},"action":"remove","lines":["password"],"id":461},{"start":{"row":104,"column":20},"end":{"row":104,"column":55},"action":"insert","lines":["config['SendEmail']['smtp-user-id']"]}],[{"start":{"row":104,"column":20},"end":{"row":104,"column":21},"action":"insert","lines":[" "],"id":462}],[{"start":{"row":104,"column":41},"end":{"row":104,"column":55},"action":"remove","lines":["'smtp-user-id'"],"id":463},{"start":{"row":104,"column":41},"end":{"row":104,"column":56},"action":"insert","lines":["'smtp-password'"]}],[{"start":{"row":106,"column":12},"end":{"row":106,"column":24},"action":"remove","lines":["sender_email"],"id":464},{"start":{"row":106,"column":12},"end":{"row":106,"column":52},"action":"insert","lines":["config['SendEmail']['smtp-sender-email']"]}],[{"start":{"row":92,"column":29},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":465},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"remove","lines":["    "],"id":466},{"start":{"row":92,"column":29},"end":{"row":93,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":92,"column":29},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":467},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":93,"column":4},"end":{"row":93,"column":44},"action":"insert","lines":["config['SendEmail']['smtp-sender-email']"],"id":468}],[{"start":{"row":93,"column":4},"end":{"row":93,"column":18},"action":"insert","lines":["receiver_email"],"id":469}],[{"start":{"row":93,"column":18},"end":{"row":93,"column":19},"action":"insert","lines":[" "],"id":470},{"start":{"row":93,"column":19},"end":{"row":93,"column":20},"action":"insert","lines":["="]}],[{"start":{"row":93,"column":20},"end":{"row":93,"column":21},"action":"insert","lines":[" "],"id":471}],[{"start":{"row":107,"column":53},"end":{"row":107,"column":54},"action":"remove","lines":[" "],"id":472}],[{"start":{"row":107,"column":53},"end":{"row":108,"column":0},"action":"insert","lines":["",""],"id":473},{"start":{"row":108,"column":0},"end":{"row":108,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":108,"column":27},"end":{"row":108,"column":28},"action":"remove","lines":[" "],"id":474}],[{"start":{"row":108,"column":27},"end":{"row":109,"column":0},"action":"insert","lines":["",""],"id":475},{"start":{"row":109,"column":0},"end":{"row":109,"column":12},"action":"insert","lines":["            "]}],[{"start":{"row":77,"column":16},"end":{"row":77,"column":17},"action":"remove","lines":["f"],"id":476}],[{"start":{"row":97,"column":45},"end":{"row":98,"column":0},"action":"insert","lines":["",""],"id":477},{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":98,"column":4},"end":{"row":98,"column":59},"action":"insert","lines":["logger.info('Start: reading message document from S3.')"],"id":478}],[{"start":{"row":98,"column":24},"end":{"row":98,"column":56},"action":"remove","lines":["reading message document from S3"],"id":479},{"start":{"row":98,"column":24},"end":{"row":98,"column":25},"action":"insert","lines":["s"]},{"start":{"row":98,"column":25},"end":{"row":98,"column":26},"action":"insert","lines":["e"]},{"start":{"row":98,"column":26},"end":{"row":98,"column":27},"action":"insert","lines":["n"]},{"start":{"row":98,"column":27},"end":{"row":98,"column":28},"action":"insert","lines":["d"]},{"start":{"row":98,"column":28},"end":{"row":98,"column":29},"action":"insert","lines":["i"]},{"start":{"row":98,"column":29},"end":{"row":98,"column":30},"action":"insert","lines":["i"]},{"start":{"row":98,"column":30},"end":{"row":98,"column":31},"action":"insert","lines":["n"]}],[{"start":{"row":98,"column":30},"end":{"row":98,"column":31},"action":"remove","lines":["n"],"id":480},{"start":{"row":98,"column":29},"end":{"row":98,"column":30},"action":"remove","lines":["i"]}],[{"start":{"row":98,"column":29},"end":{"row":98,"column":30},"action":"insert","lines":["n"],"id":481},{"start":{"row":98,"column":30},"end":{"row":98,"column":31},"action":"insert","lines":["g"]}],[{"start":{"row":98,"column":31},"end":{"row":98,"column":32},"action":"insert","lines":[" "],"id":482},{"start":{"row":98,"column":32},"end":{"row":98,"column":33},"action":"insert","lines":["e"]},{"start":{"row":98,"column":33},"end":{"row":98,"column":34},"action":"insert","lines":[","]},{"start":{"row":98,"column":34},"end":{"row":98,"column":35},"action":"insert","lines":["a"]},{"start":{"row":98,"column":35},"end":{"row":98,"column":36},"action":"insert","lines":["i"]},{"start":{"row":98,"column":36},"end":{"row":98,"column":37},"action":"insert","lines":["l"]}],[{"start":{"row":98,"column":33},"end":{"row":98,"column":34},"action":"remove","lines":[","],"id":483}],[{"start":{"row":98,"column":33},"end":{"row":98,"column":34},"action":"insert","lines":["m"],"id":484}],[{"start":{"row":111,"column":9},"end":{"row":112,"column":0},"action":"insert","lines":["",""],"id":485},{"start":{"row":112,"column":0},"end":{"row":112,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":112,"column":4},"end":{"row":112,"column":8},"action":"remove","lines":["    "],"id":486}],[{"start":{"row":112,"column":0},"end":{"row":112,"column":4},"action":"remove","lines":["    "],"id":487},{"start":{"row":111,"column":9},"end":{"row":112,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":111,"column":9},"end":{"row":112,"column":0},"action":"insert","lines":["",""],"id":488},{"start":{"row":112,"column":0},"end":{"row":112,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":112,"column":8},"end":{"row":112,"column":62},"action":"insert","lines":["logger.info('Success: read message document from S3.')"],"id":489}],[{"start":{"row":112,"column":30},"end":{"row":112,"column":59},"action":"remove","lines":["read message document from S3"],"id":490},{"start":{"row":112,"column":30},"end":{"row":112,"column":31},"action":"insert","lines":["e"]},{"start":{"row":112,"column":31},"end":{"row":112,"column":32},"action":"insert","lines":["m"]},{"start":{"row":112,"column":32},"end":{"row":112,"column":33},"action":"insert","lines":["a"]},{"start":{"row":112,"column":33},"end":{"row":112,"column":34},"action":"insert","lines":["i"]},{"start":{"row":112,"column":34},"end":{"row":112,"column":35},"action":"insert","lines":["l"]}],[{"start":{"row":112,"column":35},"end":{"row":112,"column":36},"action":"insert","lines":[" "],"id":491},{"start":{"row":112,"column":36},"end":{"row":112,"column":37},"action":"insert","lines":["s"]},{"start":{"row":112,"column":37},"end":{"row":112,"column":38},"action":"insert","lines":["e"]},{"start":{"row":112,"column":38},"end":{"row":112,"column":39},"action":"insert","lines":["n"]},{"start":{"row":112,"column":39},"end":{"row":112,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":93,"column":21},"end":{"row":93,"column":61},"action":"remove","lines":["config['SendEmail']['smtp-sender-email']"],"id":492},{"start":{"row":93,"column":21},"end":{"row":93,"column":56},"action":"insert","lines":["os.environ['SSM_PS_APPCONFIG_PATH']"]}],[{"start":{"row":93,"column":33},"end":{"row":93,"column":54},"action":"remove","lines":["SSM_PS_APPCONFIG_PATH"],"id":493},{"start":{"row":93,"column":33},"end":{"row":93,"column":55},"action":"insert","lines":["RECEIVER_EMAIL_ADDRESS"]}],[{"start":{"row":96,"column":20},"end":{"row":96,"column":60},"action":"remove","lines":["config['SendEmail']['smtp-sender-email']"],"id":494},{"start":{"row":96,"column":20},"end":{"row":96,"column":34},"action":"insert","lines":["receiver_email"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":64,"column":50},"end":{"row":64,"column":50},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":49,"state":"qqstring3","mode":"ace/mode/python"}},"timestamp":1598248601926,"hash":"aa53b58f586a07eae58fb7c39d1aafa0cb86dfae"}