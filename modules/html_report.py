from datetime import datetime

def html_reporter(domain, whois_data, port_data, tech_data, http_data):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        tech_html = ""
        if tech_data and isinstance(tech_data, dict):
            for kategori, araclar in tech_data.items():
                arac_metni = ", ".join(araclar) if isinstance(araclar, list) else araclar
                tech_html += f"<p style='margin: 5px 0;'><strong>{kategori.title()}:</strong> <span style='color: var(--success);'>{arac_metni}</span></p>"
        else:
            tech_html = "<span class='no-ports'>Herhangi bir teknoloji tespiti yapılamadı.</span>"
            
        http_satirlari = ""
        if http_data and isinstance(http_data, dict):
            for anahtar, deger in http_data.items():
                if isinstance(deger, dict):
                    for alt_anahtar, alt_deger in deger.items():
                        http_satirlari += f"<tr><td>{alt_anahtar}</td><td>{alt_deger}</td></tr>\n"
                else:
                    http_satirlari += f"<tr><td>{anahtar}</td><td>{deger}</td></tr>\n"
        else:
            http_satirlari = "<tr><td colspan='2' class='no-ports'>HTTP Başlığı bulunamadı.</td></tr>"
            
        html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SectyPy Tarama Raporu - {domain}</title>
    <style>
        :root {{
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-color: #f8fafc;
            --text-muted: #94a3b8;
            --primary: #38bdf8;
            --success: #4ade80;
            --warning: #facc15;
            --border: #334155;
        }}
        body {{
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
        }}
        header {{
            border-bottom: 2px solid var(--border);
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        h1 {{ margin: 0; color: var(--primary); font-size: 2.5rem; }}
        .meta {{ color: var(--text-muted); margin-top: 5px; }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
            gap: 20px;
        }}
        .card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        }}
        .card h2 {{
            margin-top: 0;
            color: var(--primary);
            border-bottom: 1px solid var(--border);
            padding-bottom: 10px;
            font-size: 1.4rem;
        }}
        .full-width {{
            grid-column: 1 / -1;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        th, td {{
            text-align: left;
            padding: 10px;
            border-bottom: 1px solid var(--border);
        }}
        th {{ color: var(--text-muted); font-weight: 600; }}
        .port-badge {{
            display: inline-block;
            background-color: rgba(74, 222, 128, 0.1);
            color: var(--success);
            padding: 4px 10px;
            border-radius: 6px;
            margin: 4px;
            font-family: monospace;
            font-size: 0.95rem;
            border: 1px solid rgba(74, 222, 128, 0.2);
        }}
        .no-ports {{ color: var(--warning); font-style: italic; }}
        pre {{
            background-color: #0b0f19;
            padding: 12px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Courier New', Courier, monospace;
            font-size: 0.9rem;
            border: 1px solid var(--border);
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>SectyPy Tarama Raporu</h1>
            <div class="meta">Hedef Domain: <strong>{domain}</strong> | Tarama Zamanı: {current_time}</div>
        </header>

        <div class="grid">
            <div class="card">
                <h2>WHOIS Bilgileri</h2>
                <table>
                    <tr><th>Registrar:</th><td>{whois_data.get('registrar', 'Bulunamadı')}</td></tr>
                    <tr><th>Oluşturulma:</th><td>{whois_data.get('creation_date', 'Bulunamadı')}</td></tr>
                    <tr><th>Bitiş:</th><td>{whois_data.get('expiration_date', 'Bulunamadı')}</td></tr>
                    <tr><th>Name Servers:</th><td>{', '.join(whois_data.get('name_servers', [])) if whois_data.get('name_servers') else 'Bulunamadı'}</td></tr>
                </table>
            </div>

            <div class="card">
                <h2>Web Teknolojileri</h2>
                <div style="padding-top: 10px;">
                    {tech_html}
                </div>
            </div>

            <div class="card full-width">
                <h2>Açık Portlar</h2>
                <div>
                    {''.join([f'<span class="port-badge">Port {p} (TCP)</span>' for p in port_data]) if port_data else '<span class="no-ports">Taranan aralıkta açık port bulunamadı veya sistem engelledi.</span>'}
                </div>
            </div>

            <div class="card full-width">
                <h2>HTTP Yanıt Başlıkları (Headers)</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Başlık (Header)</th>
                            <th>Değer (Value)</th>
                        </tr>
                    </thead>
                    <tbody>
                        {http_satirlari}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</body>
</html>"""
        
        with open(f"{domain}_html_report.html", "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"[+] Rapor başarıyla oluşturuldu: {domain}_html_report.html")

    except Exception as e:
        print(f"Rapor oluşturulurken bir hata meydana geldi: {e}")