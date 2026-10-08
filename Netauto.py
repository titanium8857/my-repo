from netmiko import ConnectHandler

firewall_device = {
    'device_type' : 'generic',
    'host' : '192.168.219.1',
    'username' : 'axroot',
    'password' : 'Axgate12#$',
    'port' : 2222,
    'fast_cli': False,
   
}

print(" 장비에 원격 접속을 시도합니다...")


try:
    # 2. 장비에 SSH 원격 접속
    net_connect = ConnectHandler(**firewall_device)
    
    
    output = net_connect.send_command(
        'show ip interface brief',
        cmd_verify=False,    
        read_timeout=30      
    )
    
    print("\n🚀 [장비 제어 결과 출력] 🚀")
    print(output)
    
    # 4. 안전하게 접속 종료
    net_connect.disconnect()
    print("\n✅ 조회가 성공적으로 완료되었습니다.")

except Exception as e:
    print(f"\n 조회 중 에러 발생: {e}")