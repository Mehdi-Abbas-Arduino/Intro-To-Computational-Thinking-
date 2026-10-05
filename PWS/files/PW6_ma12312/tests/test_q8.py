import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q8 import generate_ids

def xstrip(s):
    lines = s.split("\n")
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return "\n".join(lines)

def hashcode(value):
    return hashlib.sha256(str(value).encode("utf-8")).hexdigest()

q8_testcases = [
    # Visible Testcases
    ('4\nWaqar Saleem Dumbledore\nUmair Azfar Khan\nShahid Snape Hussain\nShah Jamal Alam', 'wd00000@st.habib.edu.pk\nuk00001@st.habib.edu.pk\nsh00002@st.habib.edu.pk\nsa00003@st.habib.edu.pk', True),
    ('3\nHarry Potter\nHermione Granger\nTom Marvolo Riddle', 'hp00000@st.habib.edu.pk\nhg00001@st.habib.edu.pk\ntr00002@st.habib.edu.pk', True),
    
    # Hidden Testcases
    ('5\n   xkcZ   gTDvORiap\n     glanoGzdi   OAQQpSSoE\n    mW  lRKUr\n  ETRv  QZxGNSybE\n     joFazcy    nKGHhtmJ     UmbdSgU', '22313ae59ef3e4291046d8391e2db98e206639fa4207da87981d75d889754339', False),
    ('13\n    SranT Nw   CYzK\n    EVz  iU   rAyg\n  UxXAr     BBsbLKozH\n     hTUsOFZS BGhO\n nnexNSC     LvQsGbaApK\n    RiXGfuQ InH   BrDr   DKLKBDg  \n  DkKvK    egE    yypmpOp    \n    zqjqyFTn pCO     wXwYQVsns    AXDOzhfTLp   mP \n  KXhTTh  BMjRD \n   xfY  gyXMevx   \n  kILwU  OrB yNSzLqZ   eU   SVnVil     \n  vVxExDVbS  kGVQSa  RcDGNKHi     KCzQ     \n    sYLMwKD   LjS', '2922d54cef572abf65dc365ba6fe7e644a4b149264cabd8c1fea8565b200b65f', False),
    ('129\n    NJLpzN   VDzARPBU  IbUD     \n   afzk   ampTphLy \n    wjtsq   qlOEGwk    mFbpw  LZ   zyNV     OcaWnE  qUasd   \n  Fz    JhFk jqQmzX    VlqU \n    uXJLFtgiR   YIkL IEdCF  mpcctJP fvNlkwL     \n    qUVqDOnW  ncc     EwsJ  zz  fN   \n     LmXJ rnwbsaFPd   qWiFY     \n     owcsB   SsGY   aXqLmQiy   yUl     ViS    Siue  yLQT  ZKgluwpJdf   QjUFDtoaR rTNmiiFy  JfQseq   kHpcsDAD    xZGfUi   \n fFmbJu  QDVsatmwG   fqn    jxWTdz    uqKPLt    dCnayCZvu   \n HKlcaaQXZ   Ss  HaUEf \n Tdn rlLkfg XNJR    \n     kZPOA fYK   xQbVgmQCy     \n  azuqT ttpcKxZScU LgMZHM Qs   \n   zEuu   maPeXBgUW LirbjdPb     ZbvCkIY     diz  JXeoks  idi     tJplIQvDnP  uFjDVinzV   rjyh   xLOb wHx guNxG SgGyXVcg    RNk   SFJafHyej     nqUGnSOyDT  \n   MVLBmVcA  ALEf   \n   jMz     XlOy    CMYTXULaj  FCXl     mD     \n   dtxrUMqwH GyiHBlpBXx  OrIIiKXv     ZYibNq   \n   uyt     fCSbctPD     \n  BNu    iPHfa   \n     zUzDavE QNuamMudr  cvXLJSfPwO owyzRRlG    Is  XPxI   vaUTX    XlCk  bwGMdDuKJ    \n    BcB  wxbXtIiR   Fb     upxyoXHJm     PKUD fEYpzeR    XSrxwTjgni    kFkHT    ceiFrGaS \n Fq  FePwI  OENiT   uEcSqoNiHF   dTooQVW \n   aTtGno  VQlMDls     tlj    VhnTk     QwU   JAjrdBxU JMthP     SkTgU     NWo   kixscHLwzD  zAJQPOhVJx  \n YQQzourUA     lLoUayekjm     cLRhcO     \n   ESroiQIW iIItig    \n IwePZZtg    POhhuC     vxTNywrhHb \n     MgWlQM    EkMszu   jhc  yMTpBBmyTF XAvqdoSrA \n     uASrVl     bXiTgUr  lvrW    kRz  nSk    \n     LfumIiPb     rHS     tQhDEz   \n     Sg     KSug   \n  Po   hZtEZJn   Xcj     dFXthbW  \n NzarYAfaq     Tu  DIF     dJ AdIY     \n  ckEMZFWX   dFltmCP   \n    cZoK     UNd     zeQIGAjgB     SeQbqkO     aetFwzT \n  iXnFYAzk   LHC  \n   aFJBfRBy     MOp \n     UVgPGfOAF UFcEz   RkKXoKlDA xXnMvFc   iacKtY  VLJuTWUZ \n    anZsWPGBjb    gLOrnkgS  wN    RvOdkn  YrT qLzNeZUao     \n    WVr     aRQcJga  \n   PujZ    bI    GooHIsyeA   AYjGL RMI     \n   wllFWbtBU   aHTjBy QpZGRRI    FlYqLDLlbl IRWjal  \n  OudfUw   jysTK IiyMceJb    VTayixa     XY     \n    toCYNI     cEBKV InUl    pHpXmhIa UgNA     \n     KPn   SVRAzVyCmh hY VMTdbUE    xtwxKN     Jy  mJmMI     NvYYihi XyeFuEINcA \n    OiFiblagQ     eh  qtu hymyoP    oK   wcEsYFIOvy hCcDBbLIO HQgn   \n xshHtYc imjqWD     HbUIo    Ecs     xq  DJU tZ \n     fwTCUihJk     TUADiOPca   wuOM  eviHrygyd  PRsX     cwomxEanA   rP \n  Ke     Gj   \n     mI   dOE  LooByXnh  AKlnFzTlI    tcGsfB   \n   gSMoUPiUEK nxkrJehbP    XEOsLbllU  djcEUGC   \n     UnOW JCdtT ScDIbijKOK cRIPpCK  \n  WzSghG  KCyTNnXLP YiDjvJxfpc     ia    iXVLvuM     pLrBIHcu   \n  ryeSsPOfLH   dZ  gzZH   \n   jKPxd     Ul iXoEhwNNzx     aUpHdIRH     AleZJrhj     bq  \n     qWZ   aShfxCAVhC  \n    iESvfJrF UByGerFjb    \n GruJx     yjJRV    tAKQh \n     oQzgq   Xwgaz DwVLTw     jvSsoavPln hEVhevmDc    \n   UXYVSTfoHC  UE  zUHAKna   \n  liM sdoOXTBqIN   KJcmJeFPq  \n  Tn     zXAIURpWX  kGhA     JioXGMR  QilDVqIuSm  \n     yGzuqxvP     jiEpzmVeB    \n  pRUupWwQR  rYrXxpbMwi    faLydGEXT   cIV   nHlLRp   GB   TxAQ ZHOw \n jLDZ kPiw    NqisLVFcnV   qgKcSa \n   aT    RyeiobJEk QaQaW    \n rXrPMwHO  lLEntGN    Dfhdg     qVGbFANRs  \n   aLJOQ    cfFWwZ   ZEnD   oBmgqVXUU    ghdKx   lyAcO    \n    Wo    HWVImAon   PIl   VrJNRvV  \n   ntsqEmqZbz     sRbaNzB UWACs  HPJfXGaHGM     \n  PPMbt   MWcKTQ    LGLUBqDDhR  XUP   Ura  \n    yr    IuVBLa  \n   OpJJrPVOYK     gcDLBdq  YMU     \n   KPWFo   kaDvLro   Jwz     JWHvdPTsrj   peP     magHCYvQ    hsTBiUHF  \n   HtnnLZ    DVhLPViVLF  gzSmxxmk     NhEys    SQYwFR    BHTtfxrZ     \n yYZFrH VyOreZDK    \n pEN    tYIi   GUTIBmnQ   dSuzmK   \n   GqqRW   XPEowwDxn     ikwvsDrKuY     UidrswDy    Aaeodh     gGiwSb \n    UInaNRFsYT     hXBoApo   OQARQ  FPrfxg  PCuuQs    \n    RwDqFFkih   qsybFR     \n   eRItJzPA   XuVAGT   jkiCbhgKmz   \n     SA  EunjSTU    gtMk  \n  uiJezvIwx   dGKN     dudWqXyhh     vV   gQhmFsUFFp  TiZgT   WVYo     \n     JJ     cD uOOWi   iYgfaaAQp    OSEJc HdBzytiCvq     kmM     GVuPtWXd     pI   \n    Sad   aBOv  ac    URby  \n  ZWpKS    bt  \n NtaLBMWYf FQyW     \n   JWoZo   jBJGuWp     \n     sxlJpf  JacKrvj    \n   LpBtB   cQQh    zCndaq   PexdvI  sFpdgk   \n DwMJDR   WDRXdJllp    \n    aTtBVqNUj     MEiY  gCxhoFevq    ZjFukBNFDz    \n   RVqAIoTNBd phPs    VpFoSM   \n   jtFBOm     lpBu fo   WbDHbiJyuZ  FJ    DMbIyhVqWJ     kmGhYL    ZujHfpUQ     \n ANvvcjEz     KOoMZQLGvq     DFTltbb    \n    bxEoLeQ   QYpn   BmMleH  qytysUc   XtooNoumfG ZuBZnhN     plmpTGRd   \n    wI    vAVOR WrHye     \n     dEBX   ZCswa     YzgUcYs   \n    odUGHS     LoshMcNh    \n     PIaWtXoJw    WtodX     xrXBs vCB TE Ltq     \n     lUHSnGvB  lXGJR   kp   fuqvvzv  \n wdICFfT   foQo KBKuJtvGZ     iQBf     EfWoxUyzdM     ZnEDi    \n Aus     TWmnUBEwM   \n BuM    wT  dSLjyLDiHr XFBsGttR     \n     oevYJ   kFWXxOE   fuJcnO  dbmdAXwM   Aogd  \n     kg qG     Bh    Zmm    cb   OLW   LPZt   KoV    olunuQE     \n   pXptgDhQT   mZAVArf \n    qxJVx     eojHjAeijt    \n  LmAwSaylW    wXmdkkRZ    uBa  \n     SZhd  TntZRn    ySmpocuIfF    \n    pfus    WivLICA    \n   rFBfvSqzU    KODTh   tRFtIrAr    aJp \n oi MJz \n     DhADImo  mLKPe   krlUC    \n kFWa    iO   cDFtVm   yjgbavAUh  hWeGQAkpnD  GPVHLlHa    sVxAMTgIY     \n   xDjXLWWO     CMSMtBEW     yr qsWEHkMBP   \n     qEo    NKeWptHjPI  xjuP     lTQgS    NOPtMEBd \n    uIJDk   ogCCzwgKD QGmTthpLio    OaqKrBHg  wSWJbOiKia    fagPdocz  mtYmx   \n   UQqOuLZ jGEdCcPM   PrjJVrHo \n CKwSgqYV   JIan     UyO    faBip   uXTNee  \n TAFZhvxrH    cdm \n     yeVe     jxHRW    \n     QTPWIbRwI  bKzU    \n nLDJbsExNW     aRar DNSbrEt    wWHg    bllvdZe   agRsxSWaZt     nJvjUIgGag  \n   Adx  euH    lJBjw  whwCzUn FJHmHzG tFHqkcht Dex     Vrb    \n   yZ   XLOVmE   KMylYg udlcOHIz   dpRkgbcq    klAXttJQ  JhNBOzKqcy  \n     hteUgEkwi  UxNdnS  QpFXjPePFj    FKEhANmgc   \n YwhJa bAYgmiGUD  ZHXvC  \n     WPNSg     YMavpyBPP  zAlcEK   loVJIq    BhuA   \n flS     pPPBP  TogjEysDkk iceWgle     dl    VCibObT msaXvfx     RxmGZf    YB YOfLBL qnWozf', '7e9c11d07e07367b6b1a46fb5597b4c4e9d92e758f168049cd867d35ad2a7841', False)
]

@pytest.mark.parametrize("inp, expected, visible", q8_testcases)
def test_q8(monkeypatch, capsys, inp, expected, visible):
    simulated = inp.split("\n")
    num_students = int(simulated[0].strip())
    names = iter(simulated[1:])
    monkeypatch.setattr("builtins.input", lambda: next(names))
    generate_ids(num_students)
    captured = capsys.readouterr().out.rstrip("\n")
    captured = xstrip(captured)
    if visible:
        assert captured == expected
    else:
        assert hashcode(captured) == expected
