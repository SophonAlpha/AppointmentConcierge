{"filter":false,"title":"upload_audio.py","tooltip":"/Pythonista/upload_audio.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":55,"column":11},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":390},{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":56,"column":0},"end":{"row":56,"column":4},"action":"remove","lines":["    "],"id":391}],[{"start":{"row":54,"column":10},"end":{"row":54,"column":19},"action":"remove","lines":["file_name"],"id":392},{"start":{"row":54,"column":10},"end":{"row":54,"column":37},"action":"insert","lines":["s3_prefix + '/' + file_name"]}],[{"start":{"row":32,"column":47},"end":{"row":32,"column":56},"action":"remove","lines":["s3_bucket"],"id":393},{"start":{"row":32,"column":47},"end":{"row":32,"column":56},"action":"insert","lines":["s3_prefix"]}],[{"start":{"row":35,"column":15},"end":{"row":35,"column":75},"action":"remove","lines":["This script is intended to be run from the sharing extension"],"id":394},{"start":{"row":35,"column":15},"end":{"row":35,"column":16},"action":"insert","lines":["D"]},{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["e"]},{"start":{"row":35,"column":17},"end":{"row":35,"column":18},"action":"insert","lines":["l"]},{"start":{"row":35,"column":18},"end":{"row":35,"column":19},"action":"insert","lines":["e"]},{"start":{"row":35,"column":19},"end":{"row":35,"column":20},"action":"insert","lines":["t"]},{"start":{"row":35,"column":20},"end":{"row":35,"column":21},"action":"insert","lines":["i"]},{"start":{"row":35,"column":21},"end":{"row":35,"column":22},"action":"insert","lines":["n"]},{"start":{"row":35,"column":22},"end":{"row":35,"column":23},"action":"insert","lines":["g"]}],[{"start":{"row":35,"column":23},"end":{"row":35,"column":24},"action":"insert","lines":[" "],"id":395}],[{"start":{"row":35,"column":24},"end":{"row":35,"column":25},"action":"insert","lines":["k"],"id":396},{"start":{"row":35,"column":25},"end":{"row":35,"column":26},"action":"insert","lines":["e"]},{"start":{"row":35,"column":26},"end":{"row":35,"column":27},"action":"insert","lines":["y"]},{"start":{"row":35,"column":27},"end":{"row":35,"column":28},"action":"insert","lines":["c"]},{"start":{"row":35,"column":28},"end":{"row":35,"column":29},"action":"insert","lines":["h"]},{"start":{"row":35,"column":29},"end":{"row":35,"column":30},"action":"insert","lines":["a"]},{"start":{"row":35,"column":30},"end":{"row":35,"column":31},"action":"insert","lines":["i"]},{"start":{"row":35,"column":31},"end":{"row":35,"column":32},"action":"insert","lines":["n"]}],[{"start":{"row":35,"column":32},"end":{"row":35,"column":33},"action":"insert","lines":[" "],"id":397},{"start":{"row":35,"column":33},"end":{"row":35,"column":34},"action":"insert","lines":["v"]},{"start":{"row":35,"column":34},"end":{"row":35,"column":35},"action":"insert","lines":["a"]},{"start":{"row":35,"column":35},"end":{"row":35,"column":36},"action":"insert","lines":["l"]},{"start":{"row":35,"column":36},"end":{"row":35,"column":37},"action":"insert","lines":["u"]},{"start":{"row":35,"column":37},"end":{"row":35,"column":38},"action":"insert","lines":["e"]},{"start":{"row":35,"column":38},"end":{"row":35,"column":39},"action":"insert","lines":["s"]}],[{"start":{"row":35,"column":39},"end":{"row":35,"column":40},"action":"insert","lines":[" "],"id":398},{"start":{"row":35,"column":40},"end":{"row":35,"column":41},"action":"insert","lines":["f"]},{"start":{"row":35,"column":41},"end":{"row":35,"column":42},"action":"insert","lines":["o"]},{"start":{"row":35,"column":42},"end":{"row":35,"column":43},"action":"insert","lines":["r"]}],[{"start":{"row":35,"column":43},"end":{"row":35,"column":44},"action":"insert","lines":[" "],"id":399},{"start":{"row":35,"column":44},"end":{"row":35,"column":45},"action":"insert","lines":["\\"]}],[{"start":{"row":35,"column":45},"end":{"row":35,"column":46},"action":"insert","lines":["'"],"id":400}],[{"start":{"row":35,"column":46},"end":{"row":35,"column":60},"action":"insert","lines":["'upload_audio'"],"id":401}],[{"start":{"row":35,"column":46},"end":{"row":35,"column":47},"action":"remove","lines":["'"],"id":402}],[{"start":{"row":35,"column":58},"end":{"row":35,"column":59},"action":"insert","lines":["\\"],"id":403}],[{"start":{"row":35,"column":63},"end":{"row":36,"column":0},"action":"insert","lines":["",""],"id":404},{"start":{"row":36,"column":0},"end":{"row":36,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":36,"column":8},"end":{"row":36,"column":45},"action":"insert","lines":["keychain.set_password('upload_audio',"],"id":405}],[{"start":{"row":36,"column":8},"end":{"row":36,"column":45},"action":"remove","lines":["keychain.set_password('upload_audio',"],"id":406},{"start":{"row":36,"column":8},"end":{"row":36,"column":51},"action":"insert","lines":[" keychain.delete_password(service, account)"]}],[{"start":{"row":36,"column":34},"end":{"row":36,"column":50},"action":"remove","lines":["service, account"],"id":407},{"start":{"row":36,"column":34},"end":{"row":36,"column":65},"action":"insert","lines":["'upload_audio', 'access_key_id'"]}],[{"start":{"row":36,"column":66},"end":{"row":37,"column":0},"action":"insert","lines":["",""],"id":408},{"start":{"row":37,"column":0},"end":{"row":37,"column":9},"action":"insert","lines":["         "]}],[{"start":{"row":37,"column":9},"end":{"row":37,"column":34},"action":"insert","lines":["keychain.delete_password("],"id":409}],[{"start":{"row":37,"column":34},"end":{"row":37,"column":69},"action":"insert","lines":["'upload_audio', 'secret_access_key'"],"id":410}],[{"start":{"row":37,"column":69},"end":{"row":37,"column":70},"action":"insert","lines":[")"],"id":411}],[{"start":{"row":37,"column":70},"end":{"row":38,"column":0},"action":"insert","lines":["",""],"id":412},{"start":{"row":38,"column":0},"end":{"row":38,"column":9},"action":"insert","lines":["         "]}],[{"start":{"row":38,"column":9},"end":{"row":38,"column":70},"action":"insert","lines":["keychain.delete_password('upload_audio', 'secret_access_key')"],"id":413}],[{"start":{"row":38,"column":34},"end":{"row":38,"column":69},"action":"remove","lines":["'upload_audio', 'secret_access_key'"],"id":414},{"start":{"row":38,"column":34},"end":{"row":38,"column":61},"action":"insert","lines":["'upload_audio', 's3_bucket'"]}],[{"start":{"row":38,"column":62},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":415},{"start":{"row":39,"column":0},"end":{"row":39,"column":9},"action":"insert","lines":["         "]}],[{"start":{"row":39,"column":9},"end":{"row":39,"column":62},"action":"insert","lines":["keychain.delete_password('upload_audio', 's3_bucket')"],"id":416}],[{"start":{"row":39,"column":34},"end":{"row":39,"column":61},"action":"remove","lines":["'upload_audio', 's3_bucket'"],"id":417},{"start":{"row":39,"column":34},"end":{"row":39,"column":61},"action":"insert","lines":["'upload_audio', 's3_prefix'"]}],[{"start":{"row":31,"column":67},"end":{"row":31,"column":76},"action":"remove","lines":[" (prefix)"],"id":418}],[{"start":{"row":31,"column":57},"end":{"row":31,"column":66},"action":"insert","lines":[" (prefix)"],"id":419}],[{"start":{"row":31,"column":66},"end":{"row":31,"column":67},"action":"insert","lines":[" "],"id":420}],[{"start":{"row":31,"column":57},"end":{"row":31,"column":58},"action":"remove","lines":[" "],"id":421}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":9},"action":"remove","lines":["         "],"id":422},{"start":{"row":36,"column":0},"end":{"row":36,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":36,"column":4},"end":{"row":36,"column":8},"action":"insert","lines":["    "],"id":423}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":9},"action":"remove","lines":["         "],"id":424},{"start":{"row":37,"column":0},"end":{"row":37,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":37,"column":4},"end":{"row":37,"column":8},"action":"insert","lines":["    "],"id":425}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":9},"action":"remove","lines":["         "],"id":426},{"start":{"row":38,"column":0},"end":{"row":38,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":38,"column":4},"end":{"row":38,"column":8},"action":"insert","lines":["    "],"id":427}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":9},"action":"remove","lines":["         "],"id":428},{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":8},"action":"insert","lines":["    "],"id":429}],[{"start":{"row":34,"column":0},"end":{"row":41,"column":4},"action":"remove","lines":["    if not appex.is_running_extension():","        print('Deleting keychain values for \\'upload_audio\\'.')","        keychain.delete_password('upload_audio', 'access_key_id')","        keychain.delete_password('upload_audio', 'secret_access_key')","        keychain.delete_password('upload_audio', 's3_bucket')","        keychain.delete_password('upload_audio', 's3_prefix')","        return","    "],"id":430}],[{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["",""],"id":431}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":432},{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":17,"column":0},"end":{"row":24,"column":0},"action":"insert","lines":["    if not appex.is_running_extension():","        print('Deleting keychain values for \\'upload_audio\\'.')","        keychain.delete_password('upload_audio', 'access_key_id')","        keychain.delete_password('upload_audio', 'secret_access_key')","        keychain.delete_password('upload_audio', 's3_bucket')","        keychain.delete_password('upload_audio', 's3_prefix')","        return",""],"id":433}],[{"start":{"row":24,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["","    "],"id":434}],[{"start":{"row":11,"column":43},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":435}],[{"start":{"row":10,"column":12},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":436}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":20},"action":"insert","lines":["import boto3.session"],"id":437}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":438}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":60},"action":"remove","lines":["Deleting keychain values for \\'upload_audio\\'"],"id":439},{"start":{"row":19,"column":15},"end":{"row":19,"column":16},"action":"insert","lines":["T"]},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["h"]},{"start":{"row":19,"column":17},"end":{"row":19,"column":18},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":19},"action":"insert","lines":[" "],"id":440},{"start":{"row":19,"column":19},"end":{"row":19,"column":20},"action":"insert","lines":["s"]},{"start":{"row":19,"column":20},"end":{"row":19,"column":21},"action":"insert","lines":["c"]},{"start":{"row":19,"column":21},"end":{"row":19,"column":22},"action":"insert","lines":["r"]},{"start":{"row":19,"column":22},"end":{"row":19,"column":23},"action":"insert","lines":["i"]},{"start":{"row":19,"column":23},"end":{"row":19,"column":24},"action":"insert","lines":["p"]},{"start":{"row":19,"column":24},"end":{"row":19,"column":25},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":[" "],"id":441},{"start":{"row":19,"column":26},"end":{"row":19,"column":27},"action":"insert","lines":["m"]},{"start":{"row":19,"column":27},"end":{"row":19,"column":28},"action":"insert","lines":["u"]},{"start":{"row":19,"column":28},"end":{"row":19,"column":29},"action":"insert","lines":["s"]},{"start":{"row":19,"column":29},"end":{"row":19,"column":30},"action":"insert","lines":["t"]}],[{"start":{"row":19,"column":30},"end":{"row":19,"column":31},"action":"insert","lines":[" "],"id":442},{"start":{"row":19,"column":31},"end":{"row":19,"column":32},"action":"insert","lines":["b"]},{"start":{"row":19,"column":32},"end":{"row":19,"column":33},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":33},"end":{"row":19,"column":34},"action":"insert","lines":[" "],"id":443},{"start":{"row":19,"column":34},"end":{"row":19,"column":35},"action":"insert","lines":["i"]},{"start":{"row":19,"column":35},"end":{"row":19,"column":36},"action":"insert","lines":["n"]},{"start":{"row":19,"column":36},"end":{"row":19,"column":37},"action":"insert","lines":["i"]},{"start":{"row":19,"column":37},"end":{"row":19,"column":38},"action":"insert","lines":["t"]},{"start":{"row":19,"column":38},"end":{"row":19,"column":39},"action":"insert","lines":["i"]},{"start":{"row":19,"column":39},"end":{"row":19,"column":40},"action":"insert","lines":["a"]},{"start":{"row":19,"column":40},"end":{"row":19,"column":41},"action":"insert","lines":["t"]},{"start":{"row":19,"column":41},"end":{"row":19,"column":42},"action":"insert","lines":["e"]},{"start":{"row":19,"column":42},"end":{"row":19,"column":43},"action":"insert","lines":["d"]}],[{"start":{"row":19,"column":43},"end":{"row":19,"column":44},"action":"insert","lines":[" "],"id":444}],[{"start":{"row":19,"column":44},"end":{"row":19,"column":45},"action":"insert","lines":["f"],"id":445},{"start":{"row":19,"column":45},"end":{"row":19,"column":46},"action":"insert","lines":["r"]},{"start":{"row":19,"column":46},"end":{"row":19,"column":47},"action":"insert","lines":["o"]},{"start":{"row":19,"column":47},"end":{"row":19,"column":48},"action":"insert","lines":["m"]}],[{"start":{"row":19,"column":48},"end":{"row":19,"column":49},"action":"insert","lines":[" "],"id":446},{"start":{"row":19,"column":49},"end":{"row":19,"column":50},"action":"insert","lines":["t"]},{"start":{"row":19,"column":50},"end":{"row":19,"column":51},"action":"insert","lines":["h"]},{"start":{"row":19,"column":51},"end":{"row":19,"column":52},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":52},"end":{"row":19,"column":53},"action":"insert","lines":[" "],"id":447},{"start":{"row":19,"column":53},"end":{"row":19,"column":54},"action":"insert","lines":["s"]}],[{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":["h"],"id":448},{"start":{"row":19,"column":55},"end":{"row":19,"column":56},"action":"insert","lines":["a"]},{"start":{"row":19,"column":56},"end":{"row":19,"column":57},"action":"insert","lines":["r"]},{"start":{"row":19,"column":57},"end":{"row":19,"column":58},"action":"insert","lines":["e"]}],[{"start":{"row":19,"column":53},"end":{"row":19,"column":54},"action":"insert","lines":["\\"],"id":449},{"start":{"row":19,"column":54},"end":{"row":19,"column":55},"action":"insert","lines":["'"]}],[{"start":{"row":19,"column":60},"end":{"row":19,"column":61},"action":"insert","lines":["\\"],"id":450},{"start":{"row":19,"column":61},"end":{"row":19,"column":62},"action":"insert","lines":["'"]}],[{"start":{"row":19,"column":62},"end":{"row":19,"column":63},"action":"insert","lines":[" "],"id":451}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":63},"action":"remove","lines":["The script must be initiated from the \\'share\\' "],"id":452},{"start":{"row":19,"column":15},"end":{"row":19,"column":76},"action":"insert","lines":["This script is intended to be run from the sharing extension."]}],[{"start":{"row":19,"column":76},"end":{"row":19,"column":77},"action":"remove","lines":["."],"id":453}],[{"start":{"row":20,"column":0},"end":{"row":24,"column":0},"action":"remove","lines":["        keychain.delete_password('upload_audio', 'access_key_id')","        keychain.delete_password('upload_audio', 'secret_access_key')","        keychain.delete_password('upload_audio', 's3_bucket')","        keychain.delete_password('upload_audio', 's3_prefix')",""],"id":454}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":455},{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "],"id":456}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":40},"action":"insert","lines":["my_session = boto3.session.Session()"],"id":457}],[{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"remove","lines":["m"],"id":458},{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"remove","lines":["y"]},{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"remove","lines":["_"]}],[{"start":{"row":40,"column":36},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":459},{"start":{"row":41,"column":0},"end":{"row":41,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":40,"column":36},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":460},{"start":{"row":41,"column":0},"end":{"row":41,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":40,"column":0},"end":{"row":43,"column":0},"action":"remove","lines":["    session = boto3.session.Session(","        ","        )",""],"id":461}],[{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"remove","lines":["",""],"id":462}],[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""],"id":463},{"start":{"row":39,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":39,"column":0},"end":{"row":39,"column":4},"action":"insert","lines":["    "],"id":464}],[{"start":{"row":39,"column":4},"end":{"row":39,"column":40},"action":"insert","lines":["my_session = boto3.session.Session()"],"id":465}],[{"start":{"row":39,"column":39},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":466},{"start":{"row":40,"column":0},"end":{"row":40,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":40,"column":0},"end":{"row":40,"column":9},"action":"remove","lines":["        )"],"id":467},{"start":{"row":40,"column":0},"end":{"row":42,"column":0},"action":"insert","lines":["        aws_access_key_id=access_key_id,","        aws_secret_access_key=secret_access_key)",""]}],[{"start":{"row":41,"column":47},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":468},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":45,"column":16},"end":{"row":45,"column":21},"action":"remove","lines":["boto3"],"id":469},{"start":{"row":45,"column":16},"end":{"row":45,"column":26},"action":"insert","lines":["my_session"]}],[{"start":{"row":41,"column":47},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":470},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":41,"column":47},"end":{"row":41,"column":48},"action":"insert","lines":[","],"id":471}],[{"start":{"row":41,"column":48},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":472},{"start":{"row":42,"column":0},"end":{"row":42,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":19},"action":"insert","lines":["region_name"],"id":473}],[{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":["="],"id":474}],[{"start":{"row":42,"column":20},"end":{"row":42,"column":22},"action":"insert","lines":["''"],"id":475}],[{"start":{"row":42,"column":21},"end":{"row":42,"column":31},"action":"insert","lines":["me-south-1"],"id":476}],[{"start":{"row":42,"column":32},"end":{"row":42,"column":33},"action":"insert","lines":[","],"id":477}],[{"start":{"row":42,"column":33},"end":{"row":43,"column":8},"action":"remove","lines":["","        "],"id":478},{"start":{"row":42,"column":32},"end":{"row":42,"column":33},"action":"remove","lines":[","]}],[{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"remove","lines":["",""],"id":479}],[{"start":{"row":45,"column":34},"end":{"row":46,"column":8},"action":"remove","lines":["","        "],"id":480}],[{"start":{"row":45,"column":38},"end":{"row":47,"column":47},"action":"remove","lines":[",","        aws_access_key_id=access_key_id,","        aws_secret_access_key=secret_access_key"],"id":481}],[{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"remove","lines":["",""],"id":482}],[{"start":{"row":48,"column":0},"end":{"row":59,"column":0},"action":"remove","lines":["    print()","    print(file_path)","    print()","    print(s3_bucket)","    print()","    print(s3_prefix)","    print()","    print(file_name)","    print()","    print(s3_prefix + '/' + file_name)","    print()",""],"id":483},{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":55,"column":20},"end":{"row":56,"column":0},"action":"insert","lines":["",""],"id":484},{"start":{"row":56,"column":0},"end":{"row":56,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":56,"column":4},"end":{"row":56,"column":8},"action":"remove","lines":["    "],"id":485}],[{"start":{"row":56,"column":4},"end":{"row":56,"column":5},"action":"insert","lines":["p"],"id":486},{"start":{"row":56,"column":5},"end":{"row":56,"column":6},"action":"insert","lines":["r"]},{"start":{"row":56,"column":6},"end":{"row":56,"column":7},"action":"insert","lines":["i"]},{"start":{"row":56,"column":7},"end":{"row":56,"column":8},"action":"insert","lines":["n"]},{"start":{"row":56,"column":8},"end":{"row":56,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":56,"column":8},"end":{"row":56,"column":9},"action":"remove","lines":["t"],"id":487},{"start":{"row":56,"column":7},"end":{"row":56,"column":8},"action":"remove","lines":["n"]},{"start":{"row":56,"column":6},"end":{"row":56,"column":7},"action":"remove","lines":["i"]},{"start":{"row":56,"column":5},"end":{"row":56,"column":6},"action":"remove","lines":["r"]}],[{"start":{"row":56,"column":0},"end":{"row":56,"column":5},"action":"remove","lines":["    p"],"id":488},{"start":{"row":56,"column":0},"end":{"row":57,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":16,"column":19},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":489},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]},{"start":{"row":17,"column":4},"end":{"row":17,"column":5},"action":"insert","lines":["p"]},{"start":{"row":17,"column":5},"end":{"row":17,"column":6},"action":"insert","lines":["r"]},{"start":{"row":17,"column":6},"end":{"row":17,"column":7},"action":"insert","lines":["i"]},{"start":{"row":17,"column":7},"end":{"row":17,"column":8},"action":"insert","lines":["n"]},{"start":{"row":17,"column":8},"end":{"row":17,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":17,"column":9},"end":{"row":17,"column":11},"action":"insert","lines":["()"],"id":490}]]},"ace":{"folds":[],"scrolltop":120,"scrollleft":0,"selection":{"start":{"row":18,"column":0},"end":{"row":18,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":29,"state":"start","mode":"ace/mode/python"}},"timestamp":1598462903395,"hash":"60b423f47cba85a1071b682929228413bdb39bd1"}