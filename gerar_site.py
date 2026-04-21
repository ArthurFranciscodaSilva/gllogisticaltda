

from pathlib import Path

# ====== CONFIGURAÇÕES (edite aqui se precisar) ======
CEP_ORIGEM_SEDEX  = "80420-010"
CEP_ORIGEM_TRANSP = "80530-060"
WHATSAPP          = "5541996857916"   # sem '+' nem espaços, formato wa.me

# ====== PÁGINA HTML ======
HTML_PAGE = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GL LOGISTICA LTDA — Entregas Rápidas e Malotes</title>
<meta name="description" content="GL Logística: entregas rápidas, malotes e fretes para todo Brasil. Calcule seu frete via Sedex ou Transportadora.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box}
  :root{
    --azul:#0B2A55;
    --azul-2:#143C7A;
    --laranja:#FF6A00;
    --laranja-2:#FF8C2E;
    --bg:#F6F8FC;
    --txt:#0E1A2B;
    --muted:#5C6B82;
    --card:#ffffff;
    --ok:#16a34a;
    --err:#dc2626;
    --shadow:0 10px 30px -10px rgba(11,42,85,.18);
  }
  html,body{font-family:'Inter',sans-serif;color:var(--txt);background:var(--bg);scroll-behavior:smooth}
  h1,h2,h3{font-family:'Space Grotesk',sans-serif;letter-spacing:-.02em}
  a{color:inherit;text-decoration:none}
  .container{max-width:1180px;margin:0 auto;padding:0 24px}

  /* HEADER */
  header{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.85);backdrop-filter:blur(12px);border-bottom:1px solid rgba(11,42,85,.08)}
  .nav{display:flex;align-items:center;justify-content:space-between;padding:14px 24px;max-width:1180px;margin:0 auto}
  .logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:20px;color:var(--azul)}
  .logo-mark{width:38px;height:38px;border-radius:10px;background:linear-gradient(135deg,var(--azul),var(--laranja));display:grid;place-items:center;color:#fff;font-weight:800;box-shadow:var(--shadow)}
  .nav ul{display:flex;gap:28px;list-style:none}
  .nav a{font-weight:500;color:var(--muted)}
  .nav a:hover{color:var(--azul)}
  .btn{display:inline-flex;align-items:center;gap:8px;padding:12px 22px;border-radius:999px;font-weight:600;cursor:pointer;border:0;transition:all .2s ease;font-size:15px}
  .btn-primary{background:linear-gradient(135deg,var(--laranja),var(--laranja-2));color:#fff;box-shadow:0 10px 24px -8px rgba(255,106,0,.55)}
  .btn-primary:hover{transform:translateY(-2px);box-shadow:0 14px 28px -10px rgba(255,106,0,.7)}
  .btn-ghost{background:transparent;color:var(--azul);border:1.5px solid rgba(11,42,85,.15)}
  .btn-ghost:hover{background:rgba(11,42,85,.05)}

  /* HERO */
  .hero{position:relative;overflow:hidden;padding:80px 0 100px}
  .hero::before{content:"";position:absolute;inset:0;background:
    radial-gradient(900px 500px at 85% -10%,rgba(255,106,0,.18),transparent 60%),
    radial-gradient(900px 500px at -10% 110%,rgba(11,42,85,.18),transparent 60%);
    z-index:0}
  .hero-grid{position:relative;z-index:1;display:grid;grid-template-columns:1.1fr 1fr;gap:60px;align-items:center}
  .hero h1{font-size:56px;line-height:1.05;font-weight:800;color:var(--azul)}
  .hero h1 span{background:linear-gradient(135deg,var(--laranja),var(--laranja-2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
  .hero p.lead{margin-top:22px;font-size:19px;color:var(--muted);max-width:520px;line-height:1.6}
  .hero-cta{margin-top:32px;display:flex;gap:14px;flex-wrap:wrap}
  .hero-stats{margin-top:46px;display:flex;gap:36px;flex-wrap:wrap}
  .stat strong{display:block;font-family:'Space Grotesk';font-size:32px;color:var(--azul)}
  .stat span{font-size:13px;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}
  .hero-card{background:#fff;border-radius:24px;padding:32px;box-shadow:var(--shadow);position:relative}
  .hero-card .truck{position:absolute;top:-30px;right:-20px;width:120px;height:120px;border-radius:50%;background:linear-gradient(135deg,var(--laranja),var(--laranja-2));display:grid;place-items:center;color:#fff;font-size:54px;box-shadow:0 18px 40px -10px rgba(255,106,0,.5)}
  .hero-card h3{font-size:22px;color:var(--azul);margin-bottom:18px}
  .hero-card .feat{display:flex;align-items:center;gap:12px;padding:12px 0;border-bottom:1px solid rgba(11,42,85,.06);color:var(--txt)}
  .hero-card .feat:last-child{border:0}
  .hero-card .ico{width:36px;height:36px;border-radius:10px;background:rgba(11,42,85,.07);display:grid;place-items:center;color:var(--azul);font-size:18px;flex-shrink:0}

  /* SEÇÕES */
  section{padding:80px 0}
  .section-title{text-align:center;margin-bottom:50px}
  .section-title small{display:inline-block;padding:6px 14px;background:rgba(255,106,0,.12);color:var(--laranja);border-radius:999px;font-weight:600;font-size:13px;letter-spacing:.06em;text-transform:uppercase}
  .section-title h2{font-size:42px;color:var(--azul);margin-top:14px}
  .section-title p{color:var(--muted);max-width:600px;margin:14px auto 0;font-size:17px}

  /* SERVIÇOS */
  .services{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
  .service{background:var(--card);border-radius:20px;padding:32px;box-shadow:var(--shadow);transition:all .25s ease;border:1px solid transparent}
  .service:hover{transform:translateY(-6px);border-color:rgba(255,106,0,.25)}
  .service .ico{width:56px;height:56px;border-radius:14px;background:linear-gradient(135deg,var(--azul),var(--azul-2));color:#fff;display:grid;place-items:center;font-size:26px;margin-bottom:18px}
  .service h3{font-size:21px;color:var(--azul);margin-bottom:10px}
  .service p{color:var(--muted);line-height:1.6;font-size:15px}

  /* CALCULADORA */
  #calc{background:linear-gradient(180deg,#fff 0%,#EEF3FB 100%)}
  .calc-box{background:#fff;border-radius:28px;padding:42px;box-shadow:var(--shadow);max-width:880px;margin:0 auto}
  .tipo-tabs{display:grid;grid-template-columns:1fr 1fr;gap:10px;background:rgba(11,42,85,.05);padding:6px;border-radius:14px;margin-bottom:28px}
  .tipo-tab{padding:14px;border-radius:10px;text-align:center;font-weight:600;color:var(--muted);cursor:pointer;transition:.2s;border:0;background:transparent;font-size:15px}
  .tipo-tab.active{background:#fff;color:var(--azul);box-shadow:0 4px 12px rgba(11,42,85,.1)}
  .tipo-tab .desc{display:block;font-size:11px;font-weight:500;margin-top:2px;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
  .tipo-tab.active .desc{color:var(--laranja)}

  .form-row{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px}
  .form-grp label{display:block;font-size:13px;font-weight:600;color:var(--azul);margin-bottom:8px;text-transform:uppercase;letter-spacing:.04em}
  .form-grp input,.form-grp select{width:100%;padding:14px 16px;border:1.5px solid rgba(11,42,85,.12);border-radius:12px;font-size:16px;font-family:inherit;color:var(--txt);transition:.2s;background:#fff}
  .form-grp input:focus,.form-grp select:focus{outline:0;border-color:var(--laranja);box-shadow:0 0 0 4px rgba(255,106,0,.12)}
  .origem-info{background:rgba(11,42,85,.04);border-radius:12px;padding:14px 16px;font-size:14px;color:var(--muted);margin-bottom:18px;display:flex;align-items:center;gap:10px}
  .origem-info b{color:var(--azul)}

  #erro{background:rgba(220,38,38,.1);color:var(--err);padding:14px;border-radius:12px;margin-top:14px;font-weight:500;display:none}
  #erro.show{display:block}

  #resultado{margin-top:24px;display:none}
  #resultado.show{display:block;animation:fadeIn .4s ease}
  @keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
  .res-card{background:linear-gradient(135deg,var(--azul),var(--azul-2));color:#fff;border-radius:18px;padding:28px;display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center}
  .res-info{font-size:14px;opacity:.85;margin-bottom:6px;text-transform:uppercase;letter-spacing:.06em}
  .res-rota{font-size:20px;font-weight:600;margin-bottom:4px}
  .res-prazo{font-size:14px;opacity:.85}
  .res-valor{text-align:right}
  .res-valor small{display:block;opacity:.75;font-size:13px}
  .res-valor strong{font-family:'Space Grotesk';font-size:38px;font-weight:700}
  .res-acao{margin-top:18px;text-align:center}

  /* PORQUE */
  .why{background:#fff}
  .why-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
  .why-item{text-align:center;padding:20px}
  .why-item .ico{width:64px;height:64px;border-radius:18px;margin:0 auto 16px;background:linear-gradient(135deg,var(--laranja),var(--laranja-2));color:#fff;display:grid;place-items:center;font-size:28px}
  .why-item h4{color:var(--azul);font-size:17px;margin-bottom:8px;font-family:'Space Grotesk'}
  .why-item p{color:var(--muted);font-size:14px;line-height:1.55}

  /* FOOTER */
  footer{background:var(--azul);color:#fff;padding:60px 0 30px}
  .foot-grid{display:grid;grid-template-columns:2fr 1fr 1fr;gap:50px;margin-bottom:40px}
  footer h4{font-size:16px;margin-bottom:18px;color:#fff;font-family:'Space Grotesk'}
  footer p,footer li{color:rgba(255,255,255,.7);font-size:14px;line-height:1.7}
  footer ul{list-style:none}
  footer a:hover{color:var(--laranja-2)}
  .foot-bottom{border-top:1px solid rgba(255,255,255,.12);padding-top:24px;text-align:center;font-size:13px;color:rgba(255,255,255,.6)}

  /* MODAL */
  .modal-bg{position:fixed;inset:0;background:rgba(11,26,43,.7);z-index:100;display:none;align-items:center;justify-content:center;padding:20px}
  .modal-bg.show{display:flex}
  .modal{background:#fff;border-radius:24px;max-width:560px;width:100%;max-height:90vh;overflow-y:auto;padding:36px;position:relative}
  .modal h3{color:var(--azul);font-size:24px;margin-bottom:8px}
  .modal p.sub{color:var(--muted);margin-bottom:24px;font-size:14px}
  .modal-close{position:absolute;top:18px;right:18px;background:rgba(11,42,85,.06);border:0;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:20px;color:var(--azul)}
  .modal .form-grp{margin-bottom:14px}
  .modal .form-row{margin-bottom:0}

  @media (max-width:900px){
    .hero-grid{grid-template-columns:1fr;gap:40px}
    .hero h1{font-size:38px}
    .services,.why-grid{grid-template-columns:1fr 1fr}
    .foot-grid{grid-template-columns:1fr;gap:30px}
    .nav ul{display:none}
    .res-card{grid-template-columns:1fr;text-align:center}
    .res-valor{text-align:center}
    .form-row{grid-template-columns:1fr}
    .section-title h2{font-size:32px}
  }
  @media (max-width:520px){
    .services,.why-grid{grid-template-columns:1fr}
    .calc-box{padding:26px 20px}
  }
</style>
</head>
<body>

<header>
  <div class="nav">
    <a href="#" class="logo">
      <div class="logo-mark">GL</div>
      <span>GL LOGISTICA</span>
    </a>
    <ul>
      <li><a href="#servicos">Serviços</a></li>
      <li><a href="#calc">Calcular Frete</a></li>
      <li><a href="#porque">Por que nós</a></li>
      <li><a href="#contato">Contato</a></li>
    </ul>
    <a href="#calc" class="btn btn-primary">Calcular agora →</a>
  </div>
</header>

<section class="hero">
  <div class="container hero-grid">
    <div>
      <h1>Logística <span>rápida</span> que o correio não entrega.</h1>
      <p class="lead">Entregas expressas, malotes empresariais e fretes para todo o Brasil. Tudo o que o serviço nacional não cobre — nós levamos.</p>
      <div class="hero-cta">
        <a href="#calc" class="btn btn-primary">📦 Calcular meu frete</a>
        <a href="#servicos" class="btn btn-ghost">Ver serviços</a>
      </div>
      <div class="hero-stats">
        <div class="stat"><strong>Atendimento em todo o Brasil</strong><span></span></div>
        <div class="stat"><strong>24h</strong><span>Agilidade operacional</span></div>
        <div class="stat"><strong>BR</strong><span>Rastreamento em tempo real</span></div>
      </div>
    </div>
    <div class="hero-card">
      <div class="truck">🚚</div>
      <h3>Por que escolher a GL?</h3>
      <div class="feat"><div class="ico">⚡</div><div><b>Redução de custos logísticos</b><br><small style="color:var(--muted)">Custo menor!</small></div></div>
      <div class="feat"><div class="ico">📍</div><div><b>Rastreamento em tempo real</b><br><small style="color:var(--muted)">Acompanhe via WhatsApp</small></div></div>
      <div class="feat"><div class="ico">💼</div><div><b>Otimização de rotas</b><br><small style="color:var(--muted)">Rotas fixas semanais</small></div></div>
      <div class="feat"><div class="ico">🛡️</div><div><b>Pacote segurado</b><br><small style="color:var(--muted)">Tranquilidade garantida</small></div></div>
    </div>
  </div>
</section>

<section id="servicos">
  <div class="container">
    <div class="section-title">
      <small>Nossos Serviços</small>
      <h2>Soluções logísticas completas</h2>
      <p>Do envio expresso ao frete fracionado, atendemos pessoas físicas e empresas com agilidade e segurança.</p>
    </div>
    <div class="services">
      <div class="service">
        <div class="ico">📮</div>
        <h3>Envio Sedex</h3>
        <p>Entregas rápidas para todo o Brasil com prazos garantidos. Ideal para encomendas urgentes de até 60kg.</p>
      </div>
      <div class="service">
        <div class="ico">🚛</div>
        <h3>Transportadora</h3>
        <p>Frete econômico para volumes maiores. Melhor custo-benefício para envios programados.</p>
      </div>
      <div class="service">
        <div class="ico">💼</div>
        <h3>Malote Empresarial</h3>
        <p>Coletas e entregas de documentos com rotas fixas. Atendemos contratos mensais e semanais.</p>
      </div>
    </div>
  </div>
</section>

<section id="calc">
  <div class="container">
    <div class="section-title">
      <small>Calcule online</small>
      <h2>Quanto custa seu frete?</h2>
      <p>Selecione o tipo de envio, informe o CEP de destino e o peso. Resposta em segundos.</p>
    </div>
    <div class="calc-box">
      <div class="tipo-tabs">
        <button class="tipo-tab active" data-tipo="sedex" onclick="selTipo('sedex')">📮 Via Sedex<span class="desc">Origem __SEDEX__</span></button>
        <button class="tipo-tab" data-tipo="transp" onclick="selTipo('transp')">🚛 Via Transportadora<span class="desc">Origem __TRANSP__</span></button>
      </div>

      <div class="origem-info">📍 <span><b>Origem:</b> CEP <span id="cep-origem">__SEDEX__</span> — Curitiba/PR</span></div>

      <div class="form-row">
        <div class="form-grp">
          <label>CEP de destino</label>
          <input type="text" id="cep-destino" maxlength="9" placeholder="00000-000" oninput="maskCep(this)">
        </div>
        <div class="form-grp">
          <label>Peso</label>
          <select id="peso">
            <option value="30">Até 30 kg</option>
            <option value="60">Até 60 kg</option>
          </select>
        </div>
      </div>

      <button class="btn btn-primary" id="btn-calc" onclick="calcularFrete()" style="width:100%;justify-content:center;padding:16px;font-size:16px">Calcular Frete</button>

      <div id="erro"></div>

      <div id="resultado">
        <div class="res-card">
          <div>
            <div class="res-info">Rota encontrada</div>
            <div class="res-rota" id="res-rota">—</div>
            <div class="res-prazo" id="res-prazo">—</div>
          </div>
          <div class="res-valor">
            <small>Valor do frete</small>
            <strong id="res-valor">R$ 0,00</strong>
          </div>
        </div>
        <div class="res-acao">
          <button class="btn btn-primary" onclick="abrirPagamento()" style="margin-top:18px">Continuar para pedido →</button>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="porque" class="why">
  <div class="container">
    <div class="section-title">
      <small>Diferenciais</small>
      <h2>Por que escolher a GL Logística?</h2>
    </div>
    <div class="why-grid">
      <div class="why-item"><div class="ico">⚡</div><h4>Agilidade</h4><p>Coletas e entregas no mesmo dia em rotas estratégicas.</p></div>
      <div class="why-item"><div class="ico">💰</div><h4>Preço justo</h4><p>Tabela transparente, sem taxas surpresa.</p></div>
      <div class="why-item"><div class="ico">📱</div><h4>Acompanhe online</h4><p>Atualizações de status direto no seu WhatsApp.</p></div>
      <div class="why-item"><div class="ico">🤝</div><h4>Atendimento humano</h4><p>Falamos com você — não com robôs.</p></div>
    </div>
  </div>
</section>

<footer id="contato">
  <div class="container">
    <div class="foot-grid">
      <div>
        <div class="logo" style="color:#fff;margin-bottom:14px"><div class="logo-mark">GL</div><span>GL LOGISTICA LTDA</span></div>
        <p>Logística rápida, malotes corporativos e fretes para todo o Brasil. Onde o correio não chega, a GL entrega.</p>
      </div>
      <div>
        <h4>Contato</h4>
        <ul>
          <li>📱 WhatsApp: (41) 99685-7916</li>
          <li>📍 Curitiba — PR</li>
          <li>✉️ contatogllogistica@gmail.com</li>
        </ul>
      </div>
      <div>
        <h4>Navegação</h4>
        <ul>
          <li><a href="#servicos">Serviços</a></li>
          <li><a href="#calc">Calcular Frete</a></li>
          <li><a href="#porque">Diferenciais</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">© <span id="ano"></span> GL LOGISTICA LTDA — Todos os direitos reservados.</div>
  </div>
</footer>

<!-- MODAL -->
<div class="modal-bg" id="modal">
  <div class="modal">
    <button class="modal-close" onclick="fecharModal()">×</button>
    <h3>Dados para entrega</h3>
    <p class="sub">Preencha para gerar seu pedido. O resumo será enviado pelo WhatsApp.</p>
    <div class="form-grp"><label>Nome completo</label><input type="text" id="d_n"></div>
    <div class="form-row">
      <div class="form-grp"><label>CPF</label><input type="text" id="d_cpf"></div>
      <div class="form-grp"><label>WhatsApp</label><input type="text" id="d_t" placeholder="(00) 00000-0000"></div>
    </div>
    <div class="form-grp"><label>Endereço</label><input type="text" id="d_e"></div>
    <div class="form-row">
      <div class="form-grp"><label>Número</label><input type="text" id="d_nu"></div>
      <div class="form-grp"><label>Complemento</label><input type="text" id="d_co"></div>
    </div>
    <div class="form-grp"><label>Bairro</label><input type="text" id="d_ba"></div>
    <div class="form-row">
      <div class="form-grp"><label>Cidade</label><input type="text" id="d_ci"></div>
      <div class="form-grp"><label>UF</label><input type="text" id="d_es" maxlength="2"></div>
    </div>
    <div class="form-grp"><label>CEP</label><input type="text" id="d_ce"></div>
    <div class="form-grp"><label>Descrição da encomenda</label><input type="text" id="d_desc" placeholder="Ex: Caixa pequena, documentos..."></div>
    <div class="form-grp"><label>Forma de pagamento</label>
      <select id="d_p"><option>Pix</option><option>Cartão de Crédito</option><option>Boleto</option><option>Transferência</option></select>
    </div>
    <button class="btn btn-primary" onclick="enviarWhats()" style="width:100%;justify-content:center;margin-top:10px">Enviar pedido pelo WhatsApp</button>
  </div>
</div>

<script>
const WHATSAPP = "__WHATS__";
const TABELA = {
  sedex:  { 30:{SUL:40, SUDESTE:70, "CENTRO-OESTE":70, NORDESTE:125, NORTE:125},
            60:{SUL:80, SUDESTE:140,"CENTRO-OESTE":140,NORDESTE:250, NORTE:250} },
  transp: { 30:{SUL:25, SUDESTE:50, "CENTRO-OESTE":50, NORDESTE:100, NORTE:100},
            60:{SUL:50, SUDESTE:100,"CENTRO-OESTE":100,NORDESTE:200, NORTE:200} }
};
const PRAZOS = {
  sedex:  {SUL:"3-9 dias úteis", SUDESTE:"5-15 dias úteis","CENTRO-OESTE":"5-15 dias úteis", NORDESTE:"10-30 dias úteis", NORTE:"10-30 dias úteis"},
  transp: {SUL:"2-5 dias úteis", SUDESTE:"4-10 dias úteis","CENTRO-OESTE":"4-10 dias úteis", NORDESTE:"7-20 dias úteis", NORTE:"7-20 dias úteis"}
};
const REGIOES = {
  SUL:["PR","SC","RS"], SUDESTE:["SP","RJ","MG","ES"],
  "CENTRO-OESTE":["MT","MS","GO","DF"],
  NORDESTE:["BA","SE","AL","PE","PB","RN","CE","PI","MA"],
  NORTE:["TO","PA","AP","RR","AM","AC","RO"]
};
const ORIGENS = { sedex:"__SEDEX__", transp:"__TRANSP__" };

let tipoAtual = "sedex";
let ultimoCalc = null;

document.getElementById('ano').textContent = new Date().getFullYear();

function selTipo(t){
  tipoAtual = t;
  document.querySelectorAll('.tipo-tab').forEach(b => b.classList.toggle('active', b.dataset.tipo===t));
  document.getElementById('cep-origem').textContent = ORIGENS[t];
  document.getElementById('resultado').classList.remove('show');
}

function maskCep(el){
  let v = el.value.replace(/\D/g,'').slice(0,8);
  if(v.length>5) v = v.slice(0,5)+'-'+v.slice(5);
  el.value = v;
}

function getRegiao(uf){
  for(const r in REGIOES) if(REGIOES[r].includes(uf)) return r;
  return null;
}

async function buscarDadosCep(cep){
  try{
    const r = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
    const d = await r.json();
    if(!d.erro) return {localidade:d.localidade, uf:d.uf.toUpperCase(), logradouro:d.logradouro||"", bairro:d.bairro||""};
  }catch(e){}
  try{
    const r = await fetch(`https://brasilapi.com.br/api/cep/v1/${cep}`);
    const d = await r.json();
    if(r.ok) return {localidade:d.city, uf:d.state.toUpperCase(), logradouro:d.street||"", bairro:d.neighborhood||""};
  }catch(e){}
  return null;
}

async function calcularFrete(){
  const cep = document.getElementById('cep-destino').value.replace(/\D/g,'');
  const peso = document.getElementById('peso').value;
  const btn = document.getElementById('btn-calc');
  const erro = document.getElementById('erro');
  erro.classList.remove('show');
  document.getElementById('resultado').classList.remove('show');

  if(cep.length !== 8){ erro.textContent='CEP inválido. Digite os 8 dígitos.'; erro.classList.add('show'); return; }

  btn.disabled = true; btn.textContent = '...';
  const data = await buscarDadosCep(cep);
  btn.disabled = false; btn.textContent = 'Calcular Frete';

  if(!data){ erro.textContent='CEP não encontrado. Verifique e tente novamente.'; erro.classList.add('show'); return; }

  const reg = getRegiao(data.uf);
  if(!reg){ erro.textContent='Não atendemos esta região no momento.'; erro.classList.add('show'); return; }

  const valor = TABELA[tipoAtual][peso][reg];
  const prazo = PRAZOS[tipoAtual][reg];

  ultimoCalc = {
    cep, uf:data.uf, cidade:data.localidade, bairro:data.bairro, end:data.logradouro,
    regiao:reg, peso, tipo:tipoAtual, valor, prazo
  };

  document.getElementById('res-rota').textContent = `${ORIGENS[tipoAtual]} (Curitiba/PR) → ${data.localidade}/${data.uf}`;
  document.getElementById('res-prazo').textContent = `Região ${reg} • ${prazo} • até ${peso}kg • ${tipoAtual==='sedex'?'Sedex':'Transportadora'}`;
  document.getElementById('res-valor').textContent = 'R$ ' + valor.toFixed(2).replace('.',',');
  document.getElementById('resultado').classList.add('show');
  document.getElementById('resultado').scrollIntoView({behavior:'smooth', block:'center'});
}

function abrirPagamento(){
  if(!ultimoCalc){ alert('Calcule o frete primeiro.'); return; }
  document.getElementById('d_ce').value = ultimoCalc.cep.replace(/(\d{5})(\d{3})/,'$1-$2');
  document.getElementById('d_ci').value = ultimoCalc.cidade;
  document.getElementById('d_es').value = ultimoCalc.uf;
  document.getElementById('d_e').value  = ultimoCalc.end;
  document.getElementById('d_ba').value = ultimoCalc.bairro;
  document.getElementById('modal').classList.add('show');
}
function fecharModal(){ document.getElementById('modal').classList.remove('show'); }

function enviarWhats(){
  if(!ultimoCalc){ alert('Calcule o frete primeiro.'); return; }
  const get = id => document.getElementById(id).value.trim();
  const d = {
    n:get('d_n'), cpf:get('d_cpf'), t:get('d_t'),
    e:get('d_e'), nu:get('d_nu'), co:get('d_co'), ba:get('d_ba'),
    ci:get('d_ci'), es:get('d_es'), ce:get('d_ce'),
    desc:get('d_desc'), p:get('d_p')
  };
  if(!d.n || !d.cpf || !d.t || !d.e || !d.nu || !d.ce){
    alert('Preencha pelo menos: nome, CPF, WhatsApp, endereço, número e CEP.'); return;
  }
  const tipoTxt = ultimoCalc.tipo==='sedex' ? 'SEDEX' : 'TRANSPORTADORA';
  let msg = "*NOVO PEDIDO GL LOGISTICA LTDA*%0A%0A";
  msg += "*CLIENTE:*%0A";
  msg += "• *NOME:* "+d.n+"%0A• *CPF:* "+d.cpf+"%0A• *WHATSAPP:* "+d.t+"%0A";
  msg += "• *END:* "+d.e+", "+d.nu+"%0A• *BAIRRO:* "+d.ba+"%0A";
  if(d.co) msg += "• *COMPL:* "+d.co+"%0A";
  msg += "• *CIDADE:* "+d.ci+"-"+d.es+"%0A• *CEP:* "+d.ce+"%0A%0A";
  msg += "*ENCOMENDA:*%0A";
  msg += "• *TIPO:* "+tipoTxt+"%0A";
  msg += "• *PESO:* até "+ultimoCalc.peso+"kg%0A";
  msg += "• *DESCRIÇÃO:* "+(d.desc||'-')+"%0A";
  msg += "• *PGTO:* "+d.p+"%0A%0A";
  msg += "🚚 *FRETE:* "+tipoTxt+" — "+ultimoCalc.regiao+" — "+ultimoCalc.prazo+"%0A";
  msg += "💰 *VALOR:* R$ "+ultimoCalc.valor.toFixed(2).replace('.',',');
  window.open("https://wa.me/"+WHATSAPP+"?text="+msg, '_blank');
  fecharModal();
}
</script>

</body>
</html>
"""


def gerar(arquivo_saida: str = "index.html") -> str:
    """Gera o arquivo HTML estático na pasta atual."""
    html = (HTML_PAGE
            .replace("__SEDEX__",  CEP_ORIGEM_SEDEX)
            .replace("__TRANSP__", CEP_ORIGEM_TRANSP)
            .replace("__WHATS__",  WHATSAPP))
    saida = Path(arquivo_saida)
    saida.write_text(html, encoding="utf-8")
    return str(saida.resolve())


if __name__ == "__main__":
    caminho = gerar("index.html")
    print("✅ Site gerado com sucesso!")
    print(f"   Arquivo: {caminho}")
    print("")
    print("Próximos passos:")
    print("  1) git add gerar_site.py index.html")
    print("  2) git commit -m 'site GL Logistica'")
    print("  3) git push")
    print("  4) GitHub -> Settings -> Pages -> Branch: main / root")
