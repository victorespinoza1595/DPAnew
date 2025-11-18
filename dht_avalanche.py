import requests
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor

# CONFIGURACIÓN - CAMBIA ESTO
CID = "bafkreihfbotmm26ix4jcogjzjbouw2vbqz5xbiy5ecnh37uhhlkgd4olqi"
TARGET_URL = "https://jebooksdreams.blogspot.com/"

# Lista de 75+ gateways IPFS públicos activos
GATEWAYS = [
    "https://ipfs.io",
    "https://cloudflare-ipfs.com",
    "https://dweb.link",
    "https://gateway.pinata.cloud",
    "https://ipfs.infura.io",
    "https://ipfs.eternum.io",
    "https://hardbin.com",
    "https://ipfs.jes.xxx",
    "https://ipfs.works",
    "https://ipfs.work",
    "https://ipfs.ink",
    "https://ipfsgateway.makersplace.com",
    "https://gateway.originprotocol.com",
    "https://ipfs.dtools.dev",
    "https://ipfs.fleek.co",
    "https://ipfs.best-practice.se",
    "https://ipfs.runfission.com",
    "https://ipfs.eth.aragon.network",
    "https://ipfs.anonymize.com",
    "https://ipfs.tubby.cloud",
    "https://ipfs.taytool.com",
    "https://ipfs.sloppyta.co",
    "https://ipfs.smoke.sh",
    "https://ipfs.slang.cx",
    "https://ipfs.safewatch.com",
    "https://ipfs.rhizome.org",
    "https://ipfs.rehash.com",
    "https://ipfs.ravenland.org",
    "https://ipfs.privacytools.io",
    "https://ipfs.mrh.io",
    "https://ipfs.mikerizzo.com",
    "https://ipfs.mauriciorivas.com",
    "https://ipfs.leiyun.org",
    "https://ipfs.kinematiks.com",
    "https://ipfs.jbb.one",
    "https://ipfs.iamoon.com",
    "https://ipfs.hossainkhan.com",
    "https://ipfs.hackygol.com",
    "https://ipfs.greyh.at",
    "https://ipfs.genenetwork.org",
    "https://ipfs.fun",
    "https://ipfs.fleek.co",
    "https://ipfs.eth.aragon.network",
    "https://ipfs.drink.cafe",
    "https://ipfs.davidz.xyz",
    "https://ipfs.cybernode.ai",
    "https://ipfs.crossbell.io",
    "https://ipfs.coinmarketcap.com",
    "https://ipfs.cf-ipfs.com",
    "https://ipfs.busy.org",
    "https://ipfs.arching-kaos.com",
    "https://ipfs.anonymize.com",
    "https://ipfs.alexandria.media",
    "https://ipfs.4everland.io",
    "https://ipfs.2read.net",
    "https://ipfs.1-2.dev",
    "https://gateway.pinata.cloud",
    "https://gateway.ipfs.io",
    "https://gateway.ipfs.io",
    "https://gateway.ipfs.io",
    "https://ipfs-gateway.cloud",
    "https://ipfs-gateway.cloud",
    "https://ipfs-gateway.cloud",
    "https://nftstorage.link",
    "https://w3s.link",
    "https://storry.tv",
    "https://video.oneloveipfs.com",
    "https://ipfs.decoo.io",
    "https://ipfs.4everland.io",
    "https://ipfs.chisdealhd.co.uk",
    "https://ipfs.alloyxuast.tk",
    "https://ipfs.090226.xyz",
    "https://ipfs.yt",
    "https://ipfs.litnet.work",
    "https://ipfs.vincent.wtf",
    "https://ipfs.taytool.com"
]

def provide_via_gateway(gateway_url):
    """Anuncia el CID en la DHT a través de un gateway"""
    try:
        # Endpoint del comando dht/provide
        provide_url = f"{gateway_url}/api/v0/dht/provide?arg={CID}"
        
        # Hacer la solicitud (timeout de 30 segundos)
        response = requests.post(provide_url, timeout=30)
        
        if response.status_code == 200:
            print(f"✅ {gateway_url} - CID anunciado exitosamente")
            return True
        else:
            print(f"⚠️  {gateway_url} - Error HTTP {response.status_code}")
            return False
            
    except requests.exceptions.Timeout:
        print(f"⏰ {gateway_url} - Timeout")
        return False
    except requests.exceptions.ConnectionError:
        print(f"🔌 {gateway_url} - Error de conexión")
        return False
    except Exception as e:
        print(f"❌ {gateway_url} - Error: {str(e)}")
        return False

def continuous_avalanche():
    """Ejecuta la avalancha continua de provides"""
    print("🚀 INICIANDO DHT PROVIDER AVALANCHE")
    print(f"🎯 CID: {CID}")
    print(f"🌐 Target: {TARGET_URL}")
    print(f"📊 Gateways disponibles: {len(GATEWAYS)}")
    print("=" * 60)
    
    cycle_count = 0
    successful_provides = 0
    
    while True:
        cycle_count += 1
        print(f"\n🔄 CICLO {cycle_count} - {time.strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Mezclar gateways para distribución aleatoria
        random.shuffle(GATEWAYS)
        
        # Ejecutar provides en paralelo (10 threads concurrentes)
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(provide_via_gateway, GATEWAYS))
        
        cycle_success = sum(results)
        successful_provides += cycle_success
        
        print(f"📈 Resultados ciclo: {cycle_success}/{len(GATEWAYS)} exitosos")
        print(f"📊 Total exitosos: {successful_provides}")
        
        # Esperar 5 minutos entre ciclos
        print("⏳ Esperando 5 minutos para próximo ciclo...")
        time.sleep(300)

if __name__ == "__main__":
    # Verificar que el CID y target estén configurados
    if CID == "QmTuCIDAquí" or TARGET_URL == "https://TU-PAGINA-REAL.com":
        print("❌ ERROR: Debes configurar el CID y TARGET_URL primero")
        print("1. Sube redirect.html a IPFS y obtén el CID")
        print("2. Actualiza las variables CID y TARGET_URL")
    else:
        continuous_avalanche()
