from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# List of URLs to scrape
urls = [
    "0xfd94bcca5a8d637668bacdaafa95434ec57740adbc6218296131f62fe2f73560",
    "0x2d2f524f98e0f0c5b169f683623a1431c1fdf007821d61c25780696596e380bf",
    "0xd96356ff6dfac097c3324c89e5cc59e5467ad6516b1c52365d1585ec57bb2e5e",
    "0xb4809529ad1a259f93335e63f0e99864017afaa5e75ba352576fe04cd7cb0489",
    "0x74d5cd5695a79ec321f22eca8e14847bf82e1b79cc174dd1b6cb8404af3f3ad6",
    "0xbcaeab5a5732d595f0923fad1d8394fc85fd46438963ff8b01b3ebeee8ee9836",
    "0x5d03f72260949088b8c8dc48abe96f0ac93b2a8063b42dbb9dd39f45f7072849",
    "0xd792bba59b031a0343cfb0ab36828d295dc4cbcefaf1662109a4e098c477ddf0",
    "0x2574cacabd072c8f1dcae19dac088d03034f88b8e6962a795b5ee31394e817b9",
    "0xa8247f360c4fd838f9ab60ea5a44265af6710859b31723ce6014cbe02b3f1040",
    "0xa14edaec31e1926610d46fbc291a1f00bae5c16ae2d30bb609a536f7556eb6b5",
    "0x26d08a3873a4774c4befd8e32b9d3603162191c4f1e2e6601a003e9024e61c8c",
    "0xe5d91a5e4da0aaf280b60cd45553f101a72b5f88e8b996053f6f3d0ed9c18e8d",
    "0x12198b5c9851ad9fe2a1840570f6e5a85863f57aeec1687c32fc9eb35e68c56b",
    "0xffed9812bfabf8b2cc873d91e5ff6e6d0957cd1bb66b92b81acac27a9968d59c",
    "0xe9c1463f0772b58d8a51ba16f2b35de116907709c03399e5c719c6c22fb6f0f6",
    "0xa8b51a72cd82a7b862c5c492d6d0212511cc474a3eeb5bf8ad573dff64e92239",
    "0xf8d56b6b08f87949db6efe251d694757b2a085f41778efad18d50b80efa0f9c9",
    "0xcc3ce8d1096ad6e38ae156e24efc71f0f1954cf1b57c140c469d34a2fe110cfc",
    "0xb984dec90332c0ce7e81b4e2554cdceaedeb0834d58c7f785ba38bd65ede4944",
    "0xc6510ad4dce9ab0653fd5c0b71bd8360c563b583201c2f9182118bfb137e5e28",
    "0xf11bdb7550b5d09105487061aa235a470e4dbbcfcb7e4d64d585927da42c858b",
    "0x754263eecdacdfe88e178f7770e283593deceda25058d2725380fbccb5ff2906",
    "0x4ec37f0501ce74aaf0126fcad816e45495c90ecc8227e7def8cf16272c4380e5",
    "0xdaff2721e8e7d9e25e7099e565db7906f2dd8dfe2203cf813a5142de73744cb7",
    "0x115d250200f73748e432973ee856f90a62560154337b10392937b6986f9cb3dc",
    "0x738e898c65f21af8bd1c1818743196707f7f9301ea446f32d3d26eeed6be106e",
    "0xeea143f6f721d696c37585a5b5e646a04c84bb9935270bd7898bc5afed988241",
    "0x401d631290f51b01632f243726401a88dad3e080ad674e1e48f23bf2d3b05087",
    "0xb9ff009508220c5c6dba322e9bd1533048049a75fbfb4b39895aa8730f221f5d",
    "0x273267002187d074bbc9f9c454d8600c5629fc4f5d69400ab027315a9d1ece81",
    "0x366d631ed40fe3cfb6af505b0517200589ddd3be75ab0e016db82f028eee3dd2",
    "0xe865d38ec677cac52834052cd9b6949400e0e7caf9cccb53cb745f16d1eef7c4",
    "0x721169fcb80a2a8e6d40bd0f41627f16f52d3c827540b81a0f9263aa46bd3192",
    "0x582d42124b96cbe28804d987ac7a0e6d82a5d685a80881616926a42cdeef1762",
    "0xe836ec2b5dc0fd742348aa1d9eb06c2f7f40a7668c0f9e77e1d6d9efb1f73b1f",
    "0xe9cf6c2b44d745e8c513692d3bc51ad64069f4d7ed6802a38a196f746fd5f1ee",
    "0x371e453d825e37e505f8083a105233c7c0a3d11c4272afb80b8a8c0c5c56f5ed",
    "0xa5f99bb85f866cfe4b4893cc1dc91be46cbdb56e5f74c0653f86194745634184",
    "0x31681474e085c4753b8bbbceaa4cecb736e35d40cd3806b37770ea5a8361862f",
    "0x46287b1077214283c89570f225b8c7afc44cfad90aa9f9121c7e8b4dfee9ee46",
    "0x5f5f567d898ec3085f0a5389e484762557c679033f12aa301156c44fa6b87efe",
    "0x29443bd7bf741f342a558652a6577fbb2b69129f3aa1f03503c327bb5613f70f",
    "0x9b7fcea06275faaf80ee4bac0a606e611bbf135529e3ac37eaa16311c7225a2b",
    "0x42bb8b955a87987359f9d72c6afd590a2bd8d0485e3d4a5587285909e92ee9cf",
    "0xd4eaba61887daba3781f162c1e350954ac4e7be347684b479635d26c384d5089",
    "0xa87e14c55843803d2664636c083f436261ef7d36ee25f575d25ed1eed8e1ab15",
    "0x57391bae6f252afade9726b1dcfc9808ffbfca9e257e1dcea7130051ec2ae3d8",
    "0x57767308a0f7e1a420d341a17324ac44d11c41b19133b4492a2e02721b338dd0",
    "0xc00afab05569c7e36c62715d759ca6d6f2e26b9c1750505a1439b3a4218b4e44",
    "0x3381a0c859a0ad150e0fe976e0247f4482fdefd49f6130371465a4dc643fa2f6",
    "0x92345a3445891976904adb8859a421673eb16209f5a8669b15449a91347ad54a",
    "0x2dd5685c0220edab22a0a86767993c39fd52b7ab9a608078661e068bbc3a1fd4",
    "0xa5107e50b637a1313f3392ffb382d13ef5cd6624121a6935e5417021fb17cf36",
    "0xffc6362900f7887da81f1dc07a0865b672ae5444c1f38c45929c4b6d43b8a4cc",
    "0x4309660b33bc2cedadc95973f8c982b04b4c89e78d8b7e1d61984553c0313834",
    "0x1cffadcfb924a385047156b541627ba9d62c042322f9815c6101dbfcb15e2367",
    "0x5e35425ea062fc5e0df23caa6370182b728cf0e26d0904078be8ebac5efd20b0",
    "0xd07b4b1a0e31cd7793d21a7a8866698f0522ac3b7c1ff32cdc52f778d2e6442c",
    "0xbbd34364ed1118af8afc95046af9e341a6cc47186844dad8c9eacb33c3ac2d82",
    "0x43ed89f83d1d160b8fcc12ad0eb5f6c9826f5b36ef4ebfefdd8a5089e3ab9a5e",
    "0x1a9ebc6d9bf89fc712f0654fe822de73c21ab05c4ad7691b28477a5cb33019a9",
    "0x9e7d5274ee3b6f001c77e7bc26adf5e95af2fe39806cfc05303753a8c87257d0",
    "0x186fa8a6cdf2ccb54da384854a1dfd4832524edbb1744a9f74c31001f69e0001",
    "0xc2b2c5b41524cb72fd38725d6e43839c5bbfd6bd9359df6b861443488a496a03",
    "0x15da820091fe859bc36700ec07b5c8f7323839ab0b7cf50d6cf516c6221518de",
    "0xc3bbc76eb24b81d2c43271f641f69555cf9944e19b641582f4b9e1c71529fe52",
    "0x5efc6a8cef1d5b7f1dbe8bb124a77f1a432c67e20a958035c65a175a78f54a59",
    "0xe6cc075999669735a34cc0dcc5ddae4e8b8331464a9e253cead831f9f9789dcb",
    "0x1f75d04c78c77f3b42cae549e9696d9fa453b886ea6a5ef40cb235f298abbcb5",
    "0x3eca4121cbcb18000491472ec925505c49a6afac8fbf274a383143aecd934b72",
    "0xcb4b07c27881567133bd037a350e1fb563b84c9995dd4989958f9d0fd89a9438",
    "0x42fcab5fac237fb263660cc5407505a7b0bd8c1b8c66b6f846f2d4a2ab63ab60",
    "0x90bb7e1bd86d6a0896726dc6f88fb70a6ccdc602b53f0b056f7d5324e9d09e5e",
    "0x0aac12927f0170a3191229ddc537ed1e5aec122f8dd481647bd108ca208a59b0",
    "0xdc0e5b1b5e9e5fe9ca08ab8c03164a418b595faccb76f15a39937f2c6b53a228",
    "0x218cb1f42a8228485ed6be271d67e7ea5d3f3642d1dc5bffb1b74864a543b8c0",
    "0xff4a9fd3f6a76806265badeeb5b6b6dd2489525193b84e189c695c735c2f5277",
    "0x25ffe06ca99208d52002a9a4ef8513b6f805e1a5fc651bd1f49260c9ee6a569a",
    "0xc2dacf4bf3dc07904fea1ee7e7d9f0dff6816f85f798a92f36b694896b036246",
    "0x00111c04d6553db380bac363f6016ef4ffde948d1aa53cff38fbaed0876d99af",
    "0x06c197d88b1ba960a9a990ced861e86fea5d2488c818afd98f931f7e7c96982f",
    "0x405e525ede70267bcf781b243d2543ab879237638fbc29ac87f4feb8730c7698",
    "0xd365749eb6116bf2729bef61e43301c26d776bf9ae951b0f61a49e29205c9129",
    "0x15e6deac7976b889183552890a26daa330e9b8bdf14749d1c4e2dd725f823f92",
    "0x44493d7386c07117528f30c9da12bc409e279aeadda415d9c9151749aeebe32c",
    "0x76a53acd0aca5aa108200e68bc7be964b407e8efbfd0cdb2e4fe0b45f7c38851",
    "0x79ccf253e244a9256c7bed0340cd9ce246f9fb4bfc9a6256ba98b3a73eb7bb20",
    "0xb0be7d2c433df3247e841916c912b55ddeebda3465a374b8645d66a900b20d22",
    "0xbe44981718c32888aaee034eb51d49346e26f5f0689763a10d00d094424da806",
    "0xea18089beb3c4a6c9f07499d9db931118adf464c494038c1257da5eab84ed9f5",
    "0xf98cb6e7dc424b36c8d7a0d2f54d1dc2934d82a10d0516a1d4a03a6aa7d5d188",
    "0x26ffadd2192c71660441f89c3623675e303d99a416b3af0fa0fb4b1ca277d477",
    "0xde64dae01d98cf380a5b6bfc5818bfa1b32b9c18b1d9cea7e4a38f5a6c947ec8",
    "0x335d372c0bb661769b28e1f5c90a394abdafebd3e3e1e8eae6a19572fcb05edb",
    "0x077ad0afd4f0a1585919626294adb19b2d28a1e1d988f2ec6c1f4b7b62954a6a",
    "0x7aeb211990d9aea32ccd9d19ec3ed8af8905c6ff7ac725f2f2ea3d2fd2f61ea1",
    "0xb2eca53f6bda6825e9de0c0aee054a0277dc903685bc9831e9d087c0e3d4b04c",
    "0xb9afd59b1938582d212f412cfd6170fdc95353b5d68a26b0dc9852ba35ad8e94",
    "0xcc82a77dd2938c887393f2fa6a29177ff7734b7a89d248cc3a41c7bafaf02208",
    "0x8d2fc1d3b25b6f6a89607707bcc2fc900f097e91c4c784c340f51bc039a22b6f",
    "0xfe8659debe93646164c54eac1e58574cb9dc65e9747aed054184480d5813d3e9",
    "0xa061367ecccb3d08759c4c68a796b53520c096c388f9a8c875e5b5427317c633",
    "0x291c922d6bead3d06cf342454ebf0b0d0728ab3131328ecc915cc66e3509b0bf",
    "0x42ebe45f6ed5c07e6556853df29c51fc36c70c00b54967fe8c4cf9077bb65065",
    "0x8708c2bf9e7ca738c26f13273834acbb6d866af4fa5f2bb2235cdbd908af5d36",
    "0xcb4126189d4afa54ce142d25583db8e8b8ceabacdbcfc99fdbbb0b341e93799c",
    "0xb2f855f6f3843d4e6815c0619130e581bdfd6f757d87b61361cbe31eff487cfd",
    "0xfd2782a2062469d87aef2bc949d53e96eb487b9ce70d4aa990e6305994406af3",
    "0xe8c779024c7ad2927d43c0689b2397b7eab0992453b96bfac404085c08e19cb1",
    "0x6aafaf6efbb798dd41f15343372f15ea2d98f320557483b3305eafb19b06b2cb",
    "0xdb4f6a3c1bd5009bf17e3a50f6762425a7c817747447721de6725704963bd218",
    "0xb2fb0f6975ad6fbaf37a766919f8588fec2fb8a556585e52eb78015f9005cd45",
    "0x2baf78872de738c7a6b0eb46119195ac624d2f9bf2aa52bc372789997b0e3240",
    "0xea110deeaffffc5e466a17fe80417c216807052607e679996666b305b46cc837",
    "0xb39ac6444762a42d970b42a5437b3a5290cdb0dc6aae557ac6ebbae7054c0733",
    "0xe748b113398b8a05a317533d17d5fd7ae75b2d394143994bb47f30000174d47c"
]

data_list = []

# Initialize the Selenium driver
driver = webdriver.Chrome()  # Use appropriate driver here

for url in urls:
    driver.get("https://sepolia.etherscan.io/tx/" + url)

    wait = WebDriverWait(driver, 10)

    # Use JavaScript to check if the element is visible
    script = "return window.getComputedStyle(document.getElementById('showUtcLocalDate')).getPropertyValue('visibility') === 'visible';"
    is_visible = driver.execute_script(script)

    print(is_visible)

    # Extract the desired information

    timestamp_element = wait.until(EC.visibility_of_element_located((By.ID, "showUtcLocalDate")))
    timestamp = timestamp_element.text.strip() 

    fee_eth_element = wait.until(EC.visibility_of_element_located((By.ID, "ContentPlaceHolder1_spanTxFee")))
    fee_eth = fee_eth_element.text.strip() 

    gas_price_element = wait.until(EC.visibility_of_element_located((By.ID, "ContentPlaceHolder1_spanGasPrice")))
    gas_price = gas_price_element.text.strip() 

    data_list.append({
        "Timestamp": timestamp,
        "Fee ETH": fee_eth,
        "Gas Price": gas_price
    })

# Clean up and quit the driver
driver.quit()

# Create a DataFrame from the extracted data
df = pd.DataFrame(data_list)

# Save the DataFrame to an Excel file
df.to_csv("transaction_data_2.csv", index=False)
