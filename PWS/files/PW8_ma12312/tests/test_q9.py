import ast
import hashlib
import os
import sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import q9
from q9 import *

q9_testcases = [
    # Visible Testcases
    ('  Waqar.  Saleem, Umair Azfar   Khan, Shahid Hussain,      Shah Jamal Alam', 4, ['ws00000@st.hu.edu.pk', 'uk00001@st.hu.edu.pk', 'sh00002@st.hu.edu.pk', 'sa00003@st.hu.edu.pk'], True),
    ('Harry Potter, Hermione Granger, Tom Marvolo Riddle', 3, ['hp00000@st.hu.edu.pk', 'hg00001@st.hu.edu.pk', 'tr00002@st.hu.edu.pk'], True),
    ('Dalinar Kholin, Shallan Davar, Brandon Sanderson', 3, ['dk00000@st.hu.edu.pk', 'sd00001@st.hu.edu.pk', 'bs00002@st.hu.edu.pk'], True),
    ('Harry Potter', 1, ['hp00000@st.hu.edu.pk'], True),
    ('Hari Puttar, Sattar Buksh, Maula Jutt', 3, ['hp00000@st.hu.edu.pk', 'sb00001@st.hu.edu.pk', 'mj00002@st.hu.edu.pk'], True),

    # Hidden Testcases
    ('   xkcZ   gTDvORiap,      glanoGzdi   OAQQpSSoE,     mW  lRKUr,   ETRv  QZxGNSybE,      joFazcy    nKGHhtmJ     UmbdSgU', 5, 'e358d377961235671dae97437ff8c3d6f413e1c98ac94c2e271fc870a01e9d94', False),
    ('    SranT Nw   CYzK,     EVz  iU   rAyg,   UxXAr     BBsbLKozH,      hTUsOFZS BGhO,  nnexNSC     LvQsGbaApK,     RiXGfuQ InH   BrDr   DKLKBDg  ,   DkKvK    egE    yypmpOp    ,     zqjqyFTn pCO     wXwYQVsns    AXDOzhfTLp   mP ,   KXhTTh  BMjRD ,    xfY  gyXMevx   ,   kILwU  OrB yNSzLqZ   eU   SVnVil     ,   vVxExDVbS  kGVQSa  RcDGNKHi     KCzQ     ,     sYLMwKD   LjS', 13, 'a88226214e841a6dd8d204581cfb5e6bb82970f92649c6821acac7b44c1a3248', False),
    ('    NJLpzN   VDzARPBU  IbUD     ,    afzk   ampTphLy ,     wjtsq   qlOEGwk    mFbpw  LZ   zyNV     OcaWnE  qUasd   ,   Fz    JhFk jqQmzX    VlqU ,     uXJLFtgiR   YIkL IEdCF  mpcctJP fvNlkwL     ,     qUVqDOnW  ncc     EwsJ  zz  fN   ,      LmXJ rnwbsaFPd   qWiFY     ,      owcsB   SsGY   aXqLmQiy   yUl     ViS    Siue  yLQT  ZKgluwpJdf   QjUFDtoaR rTNmiiFy  JfQseq   kHpcsDAD    xZGfUi   ,  fFmbJu  QDVsatmwG   fqn    jxWTdz    uqKPLt    dCnayCZvu   ,  HKlcaaQXZ   Ss  HaUEf ,  Tdn rlLkfg XNJR    ,      kZPOA fYK   xQbVgmQCy     ,   azuqT ttpcKxZScU LgMZHM Qs   ,    zEuu   maPeXBgUW LirbjdPb     ZbvCkIY     diz  JXeoks  idi     tJplIQvDnP  uFjDVinzV   rjyh   xLOb wHx guNxG SgGyXVcg    RNk   SFJafHyej     nqUGnSOyDT  ,    MVLBmVcA  ALEf   ,    jMz     XlOy    CMYTXULaj  FCXl     mD     ,    dtxrUMqwH GyiHBlpBXx  OrIIiKXv     ZYibNq   ,    uyt     fCSbctPD     ,   BNu    iPHfa   ,      zUzDavE QNuamMudr  cvXLJSfPwO owyzRRlG    Is  XPxI   vaUTX    XlCk  bwGMdDuKJ    ,     BcB  wxbXtIiR   Fb     upxyoXHJm     PKUD fEYpzeR    XSrxwTjgni    kFkHT    ceiFrGaS ,  Fq  FePwI  OENiT   uEcSqoNiHF   dTooQVW ,    aTtGno  VQlMDls     tlj    VhnTk     QwU   JAjrdBxU JMthP     SkTgU     NWo   kixscHLwzD  zAJQPOhVJx  ,  YQQzourUA     lLoUayekjm     cLRhcO     ,    ESroiQIW iIItig    ,  IwePZZtg    POhhuC     vxTNywrhHb ,      MgWlQM    EkMszu   jhc  yMTpBBmyTF XAvqdoSrA ,      uASrVl     bXiTgUr  lvrW    kRz  nSk    ,      LfumIiPb     rHS     tQhDEz   ,      Sg     KSug   ,   Po   hZtEZJn   Xcj     dFXthbW  ,  NzarYAfaq     Tu  DIF     dJ AdIY     ,   ckEMZFWX   dFltmCP   ,     cZoK     UNd     zeQIGAjgB     SeQbqkO     aetFwzT ,   iXnFYAzk   LHC  ,    aFJBfRBy     MOp ,      UVgPGfOAF UFcEz   RkKXoKlDA xXnMvFc   iacKtY  VLJuTWUZ ,     anZsWPGBjb    gLOrnkgS  wN    RvOdkn  YrT qLzNeZUao     ,     WVr     aRQcJga  ,    PujZ    bI    GooHIsyeA   AYjGL RMI     ,    wllFWbtBU   aHTjBy QpZGRRI    FlYqLDLlbl IRWjal  ,   OudfUw   jysTK IiyMceJb    VTayixa     XY     ,     toCYNI     cEBKV InUl    pHpXmhIa UgNA     ,      KPn   SVRAzVyCmh hY VMTdbUE    xtwxKN     Jy  mJmMI     NvYYihi XyeFuEINcA ,     OiFiblagQ     eh  qtu hymyoP    oK   wcEsYFIOvy hCcDBbLIO HQgn   ,  xshHtYc imjqWD     HbUIo    Ecs     xq  DJU tZ ,      fwTCUihJk     TUADiOPca   wuOM  eviHrygyd  PRsX     cwomxEanA   rP ,   Ke     Gj   ,      mI   dOE  LooByXnh  AKlnFzTlI    tcGsfB   ,    gSMoUPiUEK nxkrJehbP    XEOsLbllU  djcEUGC   ,      UnOW JCdtT ScDIbijKOK cRIPpCK  ,   WzSghG  KCyTNnXLP YiDjvJxfpc     ia    iXVLvuM     pLrBIHcu   ,   ryeSsPOfLH   dZ  gzZH   ,    jKPxd     Ul iXoEhwNNzx     aUpHdIRH     AleZJrhj     bq  ,      qWZ   aShfxCAVhC  ,     iESvfJrF UByGerFjb    ,  GruJx     yjJRV    tAKQh ,      oQzgq   Xwgaz DwVLTw     jvSsoavPln hEVhevmDc    ,    UXYVSTfoHC  UE  zUHAKna   ,   liM sdoOXTBqIN   KJcmJeFPq  ,   Tn     zXAIURpWX  kGhA     JioXGMR  QilDVqIuSm  ,      yGzuqxvP     jiEpzmVeB    ,   pRUupWwQR  rYrXxpbMwi    faLydGEXT   cIV   nHlLRp   GB   TxAQ ZHOw ,  jLDZ kPiw    NqisLVFcnV   qgKcSa ,    aT    RyeiobJEk QaQaW    ,  rXrPMwHO  lLEntGN    Dfhdg     qVGbFANRs  ,    aLJOQ    cfFWwZ   ZEnD   oBmgqVXUU    ghdKx   lyAcO    ,     Wo    HWVImAon   PIl   VrJNRvV  ,    ntsqEmqZbz     sRbaNzB UWACs  HPJfXGaHGM     ,   PPMbt   MWcKTQ    LGLUBqDDhR  XUP   Ura  ,     yr    IuVBLa  ,    OpJJrPVOYK     gcDLBdq  YMU     ,    KPWFo   kaDvLro   Jwz     JWHvdPTsrj   peP     magHCYvQ    hsTBiUHF  ,    HtnnLZ    DVhLPViVLF  gzSmxxmk     NhEys    SQYwFR    BHTtfxrZ     ,  yYZFrH VyOreZDK    ,  pEN    tYIi   GUTIBmnQ   dSuzmK   ,    GqqRW   XPEowwDxn     ikwvsDrKuY     UidrswDy    Aaeodh     gGiwSb ,     UInaNRFsYT     hXBoApo   OQARQ  FPrfxg  PCuuQs    ,     RwDqFFkih   qsybFR     ,    eRItJzPA   XuVAGT   jkiCbhgKmz   ,      SA  EunjSTU    gtMk  ,   uiJezvIwx   dGKN     dudWqXyhh     vV   gQhmFsUFFp  TiZgT   WVYo     ,      JJ     cD uOOWi   iYgfaaAQp    OSEJc HdBzytiCvq     kmM     GVuPtWXd     pI   ,     Sad   aBOv  ac    URby  ,   ZWpKS    bt  ,  NtaLBMWYf FQyW     ,    JWoZo   jBJGuWp     ,      sxlJpf  JacKrvj    ,    LpBtB   cQQh    zCndaq   PexdvI  sFpdgk   ,  DwMJDR   WDRXdJllp    ,     aTtBVqNUj     MEiY  gCxhoFevq    ZjFukBNFDz    ,    RVqAIoTNBd phPs    VpFoSM   ,    jtFBOm     lpBu fo   WbDHbiJyuZ  FJ    DMbIyhVqWJ     kmGhYL    ZujHfpUQ     ,  ANvvcjEz     KOoMZQLGvq     DFTltbb    ,     bxEoLeQ   QYpn   BmMleH  qytysUc   XtooNoumfG ZuBZnhN     plmpTGRd   ,     wI    vAVOR WrHye     ,      dEBX   ZCswa     YzgUcYs   ,     odUGHS     LoshMcNh    ,      PIaWtXoJw    WtodX     xrXBs vCB TE Ltq     ,      lUHSnGvB  lXGJR   kp   fuqvvzv  ,  wdICFfT   foQo KBKuJtvGZ     iQBf     EfWoxUyzdM     ZnEDi    ,  Aus     TWmnUBEwM   ,  BuM    wT  dSLjyLDiHr XFBsGttR     ,      oevYJ   kFWXxOE   fuJcnO  dbmdAXwM   Aogd  ,      kg qG     Bh    Zmm    cb   OLW   LPZt   KoV    olunuQE     ,    pXptgDhQT   mZAVArf ,     qxJVx     eojHjAeijt    ,   LmAwSaylW    wXmdkkRZ    uBa  ,      SZhd  TntZRn    ySmpocuIfF    ,     pfus    WivLICA    ,    rFBfvSqzU    KODTh   tRFtIrAr    aJp ,  oi MJz ,      DhADImo  mLKPe   krlUC    ,  kFWa    iO   cDFtVm   yjgbavAUh  hWeGQAkpnD  GPVHLlHa    sVxAMTgIY     ,    xDjXLWWO     CMSMtBEW     yr qsWEHkMBP   ,      qEo    NKeWptHjPI  xjuP     lTQgS    NOPtMEBd ,     uIJDk   ogCCzwgKD QGmTthpLio    OaqKrBHg  wSWJbOiKia    fagPdocz  mtYmx   ,    UQqOuLZ jGEdCcPM   PrjJVrHo ,  CKwSgqYV   JIan     UyO    faBip   uXTNee  ,  TAFZhvxrH    cdm ,      yeVe     jxHRW    ,      QTPWIbRwI  bKzU    ,  nLDJbsExNW     aRar DNSbrEt    wWHg    bllvdZe   agRsxSWaZt     nJvjUIgGag  ,    Adx  euH    lJBjw  whwCzUn FJHmHzG tFHqkcht Dex     Vrb    ,    yZ   XLOVmE   KMylYg udlcOHIz   dpRkgbcq    klAXttJQ  JhNBOzKqcy  ,      hteUgEkwi  UxNdnS  QpFXjPePFj    FKEhANmgc   ,  YwhJa bAYgmiGUD  ZHXvC  ,      WPNSg     YMavpyBPP  zAlcEK   loVJIq    BhuA   ,  flS     pPPBP  TogjEysDkk iceWgle     dl    VCibObT msaXvfx     RxmGZf    YB YOfLBL qnWozf', 129, 'f04cc897e0b5dce90e52a5f1aa42860b1e9b9f77ccf504a70db9ad14776af50e', False),
    ('Waqar Saleem, Umair Azfar Khan, Shah Jamal Alam, Shahid Hussain', 4, '0f0e24a02ccdc9de3806eba2dd2e0f91f309b15f0a537a8d9efd90f63356742a', False),
    ('  ALBUS Percival Dumbledore, minerva mcgonagall  ', 2, '015a69fab449dc07dc84e311b9f3b4c77751814ae35308bc624e8e8ca05522e5', False),
    ('A B, C   D, E F G', 3, '2296b8d849edb2526c5f620e55683cd7bc1b078a6458ad6b0aad4d11643b0bba', False),
    ('Jean Luc Picard, James T Kirk', 2, 'e0ca84ae751a35ddc3f879ddd8e9f7f2e45aedcac085f8a27b6b27b48ab40245', False),
    ('Ada Lovelace, Grace Brewster Murray Hopper', 2, '337038f1934483f4322131e5fe7258f1ed9c53c140657a00ec59da820b3112ae', False),
    ('Peter Parker, Miles Morales, Gwen Stacy', 3, 'f031bb52a4a8037abcec64ecd186db9616748c079fcd86648dd1ce1cb14279ae', False),
    ('Bruce Wayne, Clark Joseph Kent', 2, '84f4b315aac698bc8f4203e685530e96cb13355276f2d54dd2b3e168b1f89132', False),
]

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

def parsed_names(s):
    return [name.strip() for name in s.split(",")]

def capture_main_list(monkeypatch, capsys, st):
    monkeypatch.setattr("builtins.input", lambda: st)
    captured=[]
    sentinel=["MAIN_USED_GENERATE_IDS"]
    def fake_generate_ids(names):
        captured.append(names)
        return sentinel
    monkeypatch.setattr(q9, "generate_ids", fake_generate_ids)
    result=q9.main()
    output=capsys.readouterr().out.strip()
    assert captured, "main() must call generate_ids()."
    assert len(captured)==1
    assert output == str(sentinel)
    assert result is None
    return captured[0]

@pytest.mark.parametrize("st, lst_length, expected, visible", q9_testcases)
def test_q9_main_calls_generate_ids(monkeypatch,capsys,st,lst_length,expected,visible):
    names=capture_main_list(monkeypatch,capsys,st)
    assert isinstance(names,list)
    assert all(isinstance(x,str) for x in names)
    assert len(names)==lst_length
    assert names == parsed_names(st)

@pytest.mark.parametrize("st, lst_length, expected, visible", q9_testcases)
def test_q9_main_output(monkeypatch,capsys,st,lst_length,expected,visible):
    monkeypatch.setattr("builtins.input", lambda: st)
    result=q9.main()
    captured=capsys.readouterr().out.strip()
    assert result is None
    try:
        printed=ast.literal_eval(captured)
    except (ValueError,SyntaxError):
        raise AssertionError("main() should print the returned list.")
    if visible:
        assert printed == expected
    else:
        assert hashcode(printed) == expected

@pytest.mark.parametrize("st, lst_length, expected, visible", q9_testcases)
def test_q9_generate_ids(st,lst_length,expected,visible):
    result=generate_ids(parsed_names(st))
    assert isinstance(result,list)
    assert len(result)==lst_length
    assert all(isinstance(x,str) for x in result)
    if visible:
        assert result == expected
    else:
        assert hashcode(result) == expected
