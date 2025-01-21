lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl, llllllllllllIII, lllllllllllIlll = Exception, filter, len, __name__, list, open, set, range, print

from os import getenv as lIlIlIlIIIIIlI
from questionary import text as IIIlIIIIIllIIl
from re import match as lIlIlllIIIIlII
from itertools import permutations as lllllIllIlllIl, product as IIlIIIllIlIIIl
from openai import OpenAI as llIIIIIllIllII
IlIlIllIIIIIllIIll = [lIlIlIlIIIIIlI('OPENAI'), lIlIlIlIIIIIlI('OPENAI1'), lIlIlIlIIIIIlI('OPENAI2'), lIlIlIlIIIIIlI('OPENAI3')]
lIIIllIllllIIlIIII = [llIIIIIllIllII(api_key=IIlIlIllIlIIIIIIlI) for IIlIlIllIlIIIIIIlI in IlIlIllIIIIIllIIll]
lIIIIlIlllIlIllIlI = 0

def llllllIlIlllIIIllI():
    """Renvoie le client OpenAI actuel."""
    return lIIIllIllllIIlIIII[lIIIIlIlllIlIllIlI]

def llIlIIlllIlIIllIII():
    """Bascule vers le prochain client OpenAI dans la liste."""
    global lIIIIlIlllIlIllIlI
    lIIIIlIlllIlIllIlI = (lIIIIlIlllIlIllIlI + 1) % lllllllllllllIl(lIIIllIllllIIlIIII)

def IIIlllllIIIlIlIIII():
    llllllIllIIIlIlIlI = IIIlIIIIIllIIl('Entrez le prénom de la cible :').ask()
    lIllIIIIIIlllIIlII = IIIlIIIIIllIIl('Entrez le nom de famille de la cible :').ask()
    IIIIlIllllIIlIlIlI = IIIlIIIIIllIIl('Entrez la date de naissance (format JJMMYYYY) :').ask()
    lIllIlllIIlllIIlll = IIIlIIIIIllIIl("Entrez le prénom d'un enfant ou proche :").ask()
    llIlIlIIlIIIlllIlI = IIIlIIIIIllIIl('Entrez un mot fétiche (surnom, équipe, etc.) :').ask()
    IIIIIIIIIIlllIlIII = IIIlIIIIIllIIl('Entrez des caractères spéciaux (par ex: !@#$) séparés par des espaces :').ask()
    llIIIllllIlllIIlll = IIIlIIIIIllIIl('Entrez le numéro de département :').ask()
    return {'name': llllllIllIIIlIlIlI, 'last_name': lIllIIIIIIlllIIlII, 'birth_date': IIIIlIllllIIlIlIlI, 'child_name': lIllIlllIIlllIIlll, 'favorite_word': llIlIlIIlIIIlllIlI, 'special_chars': IIIIIIIIIIlllIlIII.split() if IIIIIIIIIIlllIlIII else ['!', '@', '#', '$', '%', '&', '*', '-', '_'], 'department_number': llIIIllllIlllIIlll}

def IlIIIIlIIIllIlIIII(llIIllIIllIllllIll, lIlIIIlIlIlIIllIII=6, IIlIIIIllIIIlIIlII=12):
    lIIlIlIIlIlIIIlIlI = [llIIllIIllIllllIll['name'], llIIllIIllIllllIll['last_name'], llIIllIIllIllllIll['birth_date'], llIIllIIllIllllIll['child_name'], llIIllIIllIllllIll['favorite_word'], llIIllIIllIllllIll['name'] + llIIllIIllIllllIll['birth_date'], llIIllIIllIllllIll['last_name'] + llIIllIIllIllllIll['birth_date'], llIIllIIllIllllIll['name'] + llIIllIIllIllllIll['last_name'], llIIllIIllIllllIll['department_number']]
    lIIlIlIIlIlIIIlIlI = llllllllllllIll(llllllllllllIIl(llllllllllllllI(None, lIIlIlIIlIlIIIlIlI)))
    llIlIlIlIlllIlIIIl = llllllllllllIIl()
    for IlIlIIlIllllIllllI in lIIlIlIIlIlIIIlIlI:
        if lIlIIIlIlIlIIllIII <= lllllllllllllIl(IlIlIIlIllllIllllI) <= IIlIIIIllIIIlIIlII and (not IlIlIIlIllllIllllI.isdigit()) and (not IlIlIIlIllllIllllI[0] in '!@#$%^&*'):
            llIlIlIlIlllIlIIIl.add(IlIlIIlIllllIllllI)
    for llIlIllIIIllIIllIl in llllllllllllIII(2, lllllllllllllIl(lIIlIlIIlIlIIIlIlI) + 1):
        for lIlIIIIlIlIIIlIIll in lllllIllIlllIl(lIIlIlIIlIlIIIlIlI, llIlIllIIIllIIllIl):
            IlIIIlIlllIIlIllIl = ''.join(lIlIIIIlIlIIIlIIll)
            if lIlIIIlIlIlIIllIII <= lllllllllllllIl(IlIIIlIlllIIlIllIl) <= IIlIIIIllIIIlIIlII and (not IlIIIlIlllIIlIllIl.isdigit()) and (not IlIIIlIlllIIlIllIl[0] in '!@#$%^&*'):
                llIlIlIlIlllIlIIIl.add(IlIIIlIlllIIlIllIl)
    for IlIlIIlIllllIllllI in lIIlIlIIlIlIIIlIlI:
        for IllIIlIIIIllllIIlI in llIIllIIllIllllIll['special_chars']:
            lIllIlIlIlIIllllII = f'{IlIlIIlIllllIllllI}{IllIIlIIIIllllIIlI}'
            if lIlIIIlIlIlIIllIII <= lllllllllllllIl(lIllIlIlIlIIllllII) <= IIlIIIIllIIIlIIlII and (not lIllIlIlIlIIllllII.isdigit()) and (not lIllIlIlIlIIllllII[0] in '!@#$%^&*'):
                llIlIlIlIlllIlIIIl.add(lIllIlIlIlIIllllII)
    for (IlIlIIlIllllIllllI, IllIIlIIIIllllIIlI) in IIlIIIllIlIIIl(lIIlIlIIlIlIIIlIlI, llIIllIIllIllllIll['special_chars']):
        lIllllIlIlllllllII = f'{IllIIlIIIIllllIIlI}{IlIlIIlIllllIllllI}{IllIIlIIIIllllIIlI}'
        if lIlIIIlIlIlIIllIII <= lllllllllllllIl(lIllllIlIlllllllII) <= IIlIIIIllIIIlIIlII and (not lIllllIlIlllllllII.isdigit()) and (not lIllllIlIlllllllII[0] in '!@#$%^&*'):
            llIlIlIlIlllIlIIIl.add(lIllllIlIlllllllII)
    IIIIIlllIllllIllIl = {IlIlIIlIllllIllllI for IlIlIIlIllllIllllI in llIlIlIlIlllIlIIIl if not IlIlIIlIllllIllllI.isdigit() and lllllllllllllIl(IlIlIIlIllllIllllI) > 2 and (not IlIlIIlIllllIllllI[0] in '!@#$%^&*')}
    IIIIIlllIllllIllIl = {IlIlIIlIllllIllllI for IlIlIIlIllllIllllI in IIIIIlllIllllIllIl if not lIlIlllIIIIlII('^\\d+\\.', IlIlIIlIllllIllllI)}
    return IIIIIlllIllllIllIl

def lIIlllllllllIIllII(lIIlIlIIlIlIIIlIlI):
    """Utilise GPT-4 pour enrichir les suggestions. Génère une wordlist fiable et longue."""
    llIIllllllllllIIll = f"En tant que générateur de mots de passe contextuels, spécialisé dans les mots de passe de personnes souvent jeunes, souvent françaises, analysez ces informations : {', '.join(lIIlIlIIlIlIIIlIlI)}. Créez une liste de mots de passe sans numérotation, en respectant ces règles:\n- Utilisez des substitutions courantes (@ pour a, 3 pour e, 1 pour i, 0 pour o)\n- Ajoutez des caractères spéciaux stratégiques (!@#$%&*)\n- Combinez les éléments de manière réaliste\n- Longueur entre 6 et 12 caractères\n- Format : un mot de passe par ligne, sans numérotation\n- Évitez les motifs trop évidents\n- Évitez les mots répétés\nImportant: Ne pas numéroter les suggestions."
    lIlIIllIllllIlllll = []
    for IlllIIlIlIlIIlIIlI in llllllllllllIII(10):
        try:
            IllIlIIlIlIllllIll = llllllIlIlllIIIllI().chat.completions.create(model='gpt-4', messages=[{'role': 'user', 'content': llIIllllllllllIIll}], temperature=0.97, max_tokens=1900, n=1)
            IllIllIlllIIlIlIIl = IllIlIIlIlIllllIll.choices[0].message.content.splitlines()
            IIlIIIlIlIIIIllIlI = [IIllIlIlIIIlIIIIlI.strip() for IIllIlIlIIIlIIIIlI in IllIllIlllIIlIlIIl if lllllllllllllIl(IIllIlIlIIIlIIIIlI.strip()) >= 6]
            lIlIIllIllllIlllll.extend(IIlIIIlIlIIIIllIlI)
            lIlIIllIllllIlllll = llllllllllllIll(llllllllllllIIl(lIlIIllIllllIlllll))
            if lllllllllllllIl(lIlIIllIllllIlllll) >= 400:
                break
        except lllllllllllllll as IlIlIIllllIlllIllI:
            lllllllllllIlll(f'Erreur avec GPT-4 sur la clé actuelle : {IlIlIIllllIlllIllI}')
            llIlIIlllIlIIllIII()
            lllllllllllIlll('Basculement vers la clé suivante.')
    return lIlIIllIllllIlllll

def IlIIlllIIIIlIIlIll():
    lllllllllllIlll('\n=== Générateur de Wordlist Contextuel ===\n')
    llIIllIIllIllllIll = IIIlllllIIIlIlIIII()
    llIlIlIlIlllIlIIIl = IlIIIIlIIIllIlIIII(llIIllIIllIllllIll)
    IlIIllllIllIlIIIII = lIIlllllllllIIllII(llllllllllllIll(llIlIlIlIlllIlIIIl))
    llIlIlIlIlllIlIIIl.update(IlIIllllIllIlIIIII)
    lllIlIlIIllIllIllI = IIIlIIIIIllIIl('Nom du fichier pour sauvegarder la wordlist :').ask()
    with llllllllllllIlI(lllIlIlIIllIllIllI, 'w') as IIIllIIlllIlIllIll:
        IIIllIIlllIlIllIll.write('\n'.join(llIlIlIlIlllIlIIIl))
    lllllllllllIlll(f'Wordlist sauvegardée sous {lllIlIlIIllIllIllI}')
if lllllllllllllII == '__main__':
    IlIIlllIIIIlIIlIll()