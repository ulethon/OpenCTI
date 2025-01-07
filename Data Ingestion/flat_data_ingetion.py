from pycti import OpenCTIApiClient

lst =["460f517bb781a5410d59ebd1014ddcbd","1e6ed52b8f605fa08806483110bd37a1","7d6064686a2bceadabcce7d3d4c591ee","209eb304a3cbfded792b16600843fa7c","ba0232aed7bcd79964dc16a185093808","0e94c94b27e2edde29ac7b442dfe6cd6","41f744ee9ace2e6ff6835e8e3c2bd684","028bd60f808738f4f88d17554429333a","17fbe3c4a11a542b8075ff4472f91f1c","2f85ca2023f03b2b0f7b68de39b4c857","1f1e33a0c4df5d0725d7ea219dd51fd9","7814b4b4940553c9242186b03c1db071","7cd521ed2045e33a1e7bc5c45c15648d","d687769ea74fb2348d93d4f6c4c016e4","6ac6c65c5d68fc5773e4a51a947d716a","69502f6c03387656adf97e4845381514","943e34ee467d91087fa1ba6ef7edd3a0","2a3d9afdf96fa3a9ecd4a6e718167e99","d785b3a639baa98b8f63c123b1aeb2d4","efc6a2ca17db5a74f051c22624e8fc3e","3482e8b10fca532fdd2d4017226b6c53","734a6e1db9c21e9bebf26de238255383","dc1f9ba753fb2ce43405fd7c6b0efe88","fcee849764e2989ca502ce2f1ebb6e3e","e5534b800e0217d796bd9d7bfffc525b","486ee309bd63d81443a93f9794280cad","4a88ca878c08196ac0da457105434799","9968354843c95350af191784d154fe67","5089dfcef1e73b768e0a4f38940e8be0","7fa3555f7f64cebeee75bf3502929538","5c5b990373930e4d740f65aa2d786770","0ef19e76d10430b6baaa262218162a10","a95ff5df8887fea1a8b0f772dd3a2169","181da521da2fbd0c386ad1f51fb536eb","7271870f799a60d1643accb6049dd6b2","2290fb0ffb1eebd3d08d99e973f2163b"]

api_url="http://localhost:8080"
api_token = "opencti ui auth token"
opencti_api_client = OpenCTIApiClient(api_url, api_token)

# for ip in lst:
# 	opencti_api_client.stix_cyber_observable.create(simple_observable_key="IPv4-Addr.value", simple_observable_value=ip)
# 	print(ip)
# 	print("ingested")

def MD5(hash):
    hs='ae11fd697ec92c7c98de3fac23aba525'
    if len(hash)==len(hs) and hash.isdigit()==False and hash.isalpha()==False and hash.isalnum()==True:
        print("MD5 - "+hash)

observable = opencti_api_client.stix_cyber_observable.create(observableData={"type": "file","hashes": {"md5": "fcd76de79819813b631d949b18b1e996","sha-1": "e08b42d92fa579c095834909b893d49259b158be","sha-256": "7cca822e0fdfeca033762213bf16a3f04d7cac8c345f84a0d740324d97f671c0"}})

for hash in lst:
	observable = opencti_api_client.stix_cyber_observable.create(
    observableData={
        "type": "file",
        "hashes": {
            "md5": hash
        },
    }
)
	print(hash)
	print("ingested")
