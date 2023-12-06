import os

seq_col1 = ['(Dal)', '(Dar)', '(Das)', '(Dcy)', '(Dgl)', '(Dgn)', '(Dhi)', '(Dil)', '(Dle)', '(Dly)', '(Dpn)', '(Dpr)',
            '(Dsg)', '(Dsn)', '(Dth)', '(Dtr)', '(Dty)', '(Dva)', '(Med)', '(Val)', '(Ala)', '(Arg)', '(Asn)', '(Asp)',
            '(Cys)', '(Gln)', '(Glu)', '(Gly)', '(His)', '(Ile)', '(Leu)', '(Lys)', '(Met)', '(Phe)', '(Pro)', '(Ser)',
            '(Thr)', '(Trp)', '(Tyr)']
seq_col2 = ['(1032)','(1036)','(1148)','(1149)','(1190)','(1230)','(1309)','(1413)','(1470)','(1671)','(1741)','(1779)',
            '(1781)','(1988)','(1990)','(2085)','(2116)','(2649)','(2663)','(2676)','(2677)','(2989)','(2PAL)','(3214)',
            '(3378)','(3523)','(3921)','(3PAL)','(4490)','(449R)','(4975)','(4PAL)','(5188)','(5279)','(5873)','(5905)',
            '(5916)','(6402)','(7185)','(7423)','(7549)','(7611)','(7981)','(8012)','(801M)','(801R)','(8086)','(8575)',
            '(8616)','(9369)','(9393)','(9816)','(AAD)','(ABU)','(AC3C)','(AC4C)','(AC5C)','(AC6C)','(AHYP)','(AIB)',
            '(ALLE)','(ATHR)','(CMB)','(D2PA)','(D3PA)','(D4PA)','(DAAD)','(DABU)','(DAHY)','(DALL)','(DATH)','(DF2F)',
            '(DF3C)','(DF3F)','(DF4F)','(DFF5)','(DHPH)','(DHSE)','(DNLE)','(DNTY)','(DNVA)','(DPHG)','(DPIP)','(DTBU)',
            '(DTIC)','(DTLE)','(F2CL)','(F2F)','(F3CL)','(F3F)','(F4F)','(FF5)','(HPHE)','(HSE)','(NLE)','(NTYR)',
            '(NVA)','(OIC)','(PHG)','(PIP)','(TBUA)','(TIC)','(1030)','(1107)','(1111)','(1217)','(1228)','(2159)',
            '(2THI)','(3THI)','(4984)','(5553)','(7212)','(7707)','(9049)','(AMF)','(AML)','(AMP)','(AMV)','(AMY)',
            '(CBN)','(CM)','(CPH)','(D2TH)','(DAMF)','(DAML)','(DAMP)','(DAMV)','(DAMY)','(DCBN)','(DMO2)','(DPEN)',
            '(DTZA)','(MO2)','(PEN)','(TZA)','(1027)','(121t)','(1482)','(1633)','(1706)','(1NAL)','(2521)','(252R)',
            '(2NAL)','(3060)','(3346)','(4350)','(9929)','(BIP)','(BPA)','(CHA)','(CHG)','(CIT)','(CPA)','(CPRG)',
            '(D1NA)','(D2NA)','(DAB)','(DAP)','(DBIP)','(DBPA)','(DCHA)','(DCHG)','(DCIT)','(DCPA)','(DCPR)','(DDAB)',
            '(DDAP)','(DDIP)','(DF4N)','(DHAR)','(DIP)','(DPRA)','(F4N)','(HARG)','(LDOP)','(ORN)','(PRA)','(AMS)',
            '(DAMS)','(Dal)', '(Dar)', '(Das)', '(Dcy)', '(Dgl)', '(Dgn)', '(Dhi)', '(Dil)', '(Dle)', '(Dly)', '(Dpn)',
            '(Dpr)','(Dsg)', '(Dsn)', '(Dth)', '(Dtr)', '(Dty)', '(Dva)', '(Med)', '(Val)', '(Ala)', '(Arg)', '(Asn)',
            '(Asp)', '(Cys)', '(Gln)', '(Glu)', '(Gly)', '(His)', '(Ile)', '(Leu)', '(Lys)', '(Met)', '(Phe)', '(Pro)',
            '(Ser)', '(Thr)', '(Trp)', '(Tyr)','(Aly)','(HLYS)','(174R)','(OICR)','(ADAB)','(ADAP)','(ADDA)','(ADDB)',
            '(ADDO)','(AORN)','(DORN)','(CB42)','(DAMC)', '(1MDT)', '(1MLT)', '(22A1)', '(22A2)', '(22CD)', '(22CL)',
            '(24CD)', '(24CL)', '(24FD)', '(24FL)', '(2ADG)', '(2ALG)', '(2BDP)', '(2BLP)', '(3BDP)', '(3BLP)',
            '(2CDP)', '(2CLP)', '(2CLG)', '(CDS1)', '(2DDP)', '(2DLP)', '(2FDP)', '(2FLP)', '(2MDS)', '(2MLS)',
            '(Diva)', '(LIS2)', '(31ND)', '(31NL)', '(32ND)', '(32NL)', '(32PD)', '(32PL)', '(32TD)', '(32TL)',
            '(33PD)', '(33PL)', '(34PD)', '(34PL)', '(3CDA)', '(3CLA)', '(AC33)', '(AS42)', '(3CDP)', '(L3CP)',
            '(3CLP)', '(D3CP)', '(D4CP)', '(L4CP)', '(D2CP)', '(L2CP)', '(3DDA)', '(3DLA)', '(3DDC)', '(3DLC)',
            '(3DDP)', '(L4DP)', '(3FDP)', '(3FLP)', '(3TBD)', '(3TBL)', '(3HDT)', '(4DLP)', '(DTLE)', '(NTBL)',
            '(4ADP)', '(4ALP)', '(4BDP)', '(4BLP)', '(4CDP)', '(4CLP)', '(4FDP)', '(4FLP)', '(4IDP)', '(4ILP)',
            '(4MDP)', '(4MLP)', '(4NDP)', '(4NLP)', '(5ODP)', '(5OLP)', '(CX76)', '(L3CA)', '(DNTY)', '(LNTY)',
            '(N2F9)', '(N9F9)', '(NF4B)', '(NT4P)', '(NT33)', '(NT3A)', '(AMLP)', '(AMDP)', '(3MDP)', '(3MLP)',
            '(NF5P)', '(NTB3)', '(NMDA)', '(NMLA)', '(NLF9)', '(NP3R)', '(2MDH)', '(2MPH)', '(2MDP)', '(2MLP)',
            '(3MDI)', '(3MLI)', '(2TDP)', '(2TLP)', '(3TLP)', '(3TDP)', '(4TDP)', '(4TLP)', '(3DLP)', '(NF4P)',
            '(2PLG)', '(22A4)', '(2SHG)', '(2T3Y)', '(31T4)', '(33D1)', '(33H4)', '(35B2)', '(3ALA)', '(3B4Y)',
            '(3BLT)', '(3BTY)', '(3C4H)', '(3DLT)', '(3FLT)', '(3HLP)', '(3ILT)', '(3MLA)', '(3MLH)', '(3NLP)',
            '(3PLA)', '(3SLA)', '(4APH)', '(4TBA)', '(4TBL)', '(5HLT)', '(6CLT)', '(AM3H)', '(BCLA)', '(D2DG)',
            '(DENC)', '(DHOP)', '(L34D)', '(NT56)', '(LBCA)', '(LHOA)', '(LHOP)', '(LMSM)', '(MDAR)', '(NCLG)',
            '(N3D3)', '(N4F9)', '(N6AL)', '(N6F9)', '(NA9F)', '(NTB6)', '(NTBH)', '(NCLL)', '(NDAS)', '(NELG)',
            '(NF24)', '(NF5V)', '(NF33)', '(NF6A)', '(NFDA)', '(NFSA)', '(OMLS)', '(NMLP)', '(NMTY)', '(NMLS)',
            '(NMLT)', '(NPLA)', '(NTBO)', '(O2DL)', '(OALS)', '(OPLS)', '(OPLT)', '(OTBD)', '(S2PL)', '(SADC)',
            '(S3HL)', '(SBLC)', '(SPLC)', '(SCLC)', '(NFSM)', '(AMLT)', '(NF2D)']
seq_col3 = ['(Dal)', '(Dar)', '(Das)', '(Dcy)', '(Dgl)', '(Dgn)', '(Dhi)', '(Dil)', '(Dle)', '(Dly)', '(Dpn)', '(Dpr)',
            '(Dsg)', '(Dsn)', '(Dth)', '(Dtr)', '(Dty)', '(Dva)', '(Med)', '(Val)', '(Ala)', '(Arg)', '(Asn)', '(Asp)',
            '(Cys)', '(Gln)', '(Glu)', '(Gly)', '(His)', '(Ile)', '(Leu)', '(Lys)', '(Met)', '(Phe)', '(Pro)', '(Ser)',
            '(Thr)', '(Trp)', '(Tyr)','(AIB)','(AMLR)','(AMDR)','(AMLN)','(AMDN)','(AMLD)','(AMDD)','(AMLC)','(AMDC)',
            '(AMLQ)','(AMDQ)','(AMLE)','(MADE)','(AMLH)','(AMRH)','(AMLI)','(AMDI)','(AMLL)','(AMDL)','(AMDW)','(AMLW)',
            '(AMLM)','(AMDM)','(AMLF)','(AMDF)','(AMLP)','(AMDP)','(AMLS)','(AMDS)','(AMLT)','(AMIT)','(AMAT)','(AMDT)',
            '(AMLY)','(AMDY)','(AMLV)','(AMDV)','(AMLK)','(AMDK)']
seq_col4 = ['(Cys)','(Dcy)']
seq_col5 = ['(Cys)']
seq_col6 = ['(Dcy)']
seq_col7 = ['(Lys)','(Dly)']
seq_col8 = ['(Lys)']
seq_col9 = ['(Dly)']
seq_col10 = ['(1MDT)', '(1MLT)', '(22A1)', '(22A2)', '(22CD)', '(22CL)', '(24CD)', '(24CL)', '(24FD)', '(24FL)',
             '(2ADG)', '(2ALG)', '(2BDP)', '(2BLP)', '(3BDP)', '(3BLP)', '(2CDP)', '(2CLP)', '(2CLG)', '(CDS1)',
             '(2DDP)', '(2DLP)', '(2FDP)', '(2FLP)', '(2MDS)', '(2MLS)', '(Diva)', '(LIS2)', '(31ND)', '(31NL)',
             '(32ND)', '(32NL)', '(32PD)', '(32PL)', '(32TD)', '(32TL)', '(33PD)', '(33PL)', '(34PD)', '(34PL)',
             '(3CDA)', '(3CLA)', '(AC33)', '(AS42)', '(3CDP)', '(L3CP)', '(3CLP)', '(D3CP)', '(D4CP)', '(L4CP)',
             '(D2CP)', '(L2CP)', '(3DDA)', '(3DLA)', '(3DDC)', '(3DLC)', '(3DDP)', '(L4DP)', '(3FDP)', '(3FLP)',
             '(3TBD)', '(3TBL)', '(3HDT)', '(4DLP)', '(DTLE)', '(NTBL)', '(4ADP)', '(4ALP)', '(4BDP)', '(4BLP)',
             '(4CDP)', '(4CLP)', '(4FDP)', '(4FLP)', '(4IDP)', '(4ILP)', '(4MDP)', '(4MLP)', '(4NDP)', '(4NLP)',
             '(5ODP)', '(5OLP)', '(CX76)', '(L3CA)', '(DNTY)', '(LNTY)', '(N2F9)', '(N9F9)', '(NF4B)', '(NT4P)',
             '(NT33)', '(NT3A)', '(AMLP)', '(AMDP)', '(3MDP)', '(3MLP)', '(NF5P)', '(NTB3)', '(NMDA)', '(NMLA)',
             '(NLF9)', '(NP3R)', '(2MDH)', '(2MPH)', '(2MDP)', '(2MLP)', '(3MDI)', '(3MLI)', '(2TDP)', '(2TLP)',
             '(3TLP)', '(3TDP)', '(4TDP)', '(4TLP)', '(3DLP)', '(NF4P)', '(2PLG)', '(22A4)', '(2SHG)', '(2T3Y)',
             '(31T4)', '(33D1)', '(33H4)', '(35B2)', '(3ALA)', '(3B4Y)', '(3BLT)', '(3BTY)', '(3C4H)', '(3DLT)',
             '(3FLT)', '(3HLP)', '(3ILT)', '(3MLA)', '(3MLH)', '(3NLP)', '(3PLA)', '(3SLA)', '(4APH)', '(4TBA)',
             '(4TBL)', '(5HLT)', '(6CLT)', '(AM3H)', '(BCLA)', '(D2DG)', '(DENC)', '(DHOP)', '(L34D)', '(NT56)',
             '(LBCA)', '(LHOA)', '(LHOP)', '(LMSM)', '(MDAR)', '(NCLG)', '(N3D3)', '(N4F9)', '(N6AL)', '(N6F9)',
             '(NA9F)', '(NTB6)', '(NTBH)', '(NCLL)', '(NDAS)', '(NELG)', '(NF24)', '(NF5V)', '(NF33)', '(NF6A)',
             '(NFDA)', '(NFSA)', '(OMLS)', '(NMLP)', '(NMTY)', '(NMLS)', '(NMLT)', '(NPLA)', '(NTBO)', '(O2DL)',
             '(OALS)', '(OPLS)', '(OPLT)', '(OTBD)', '(S2PL)', '(SADC)', '(S3HL)', '(SBLC)', '(SPLC)', '(SCLC)',
             '(NFSM)', '(AMLT)', '(NF2D)']

print("\nsequence generator\n")

while True:
    print('Please enter the length of the sequence\n')
    datal11 = int(input())
    seq_con = ''
    for i11 in range(datal11):
        if (i11+1) != datal11:
            seq_con = seq_con + 'seq' + str(i11+1) + '--'
        if (i11+1) == datal11:
            seq_con = seq_con + 'seq' + str(i11 + 1)
    print('Sequence composition：')
    print(seq_con + '\n')

    print('Please enter the sequence number to select the basic amino acid set or directly enter the set manually '
          'to specify the amino acid set to be used for each position of the sequence.\n')
    print('Set of amino acids：\n1: 20 natural amino acids + 19 D-amino acids (39)'
          '\n2: all amino acids in the library (425)'
          '\n3: 39 amino acids and their corresponding methylated amino acids (78)'
          '\n4: Cysteine (Cys, Dcy) (2)'
          '\n5: Cys (1)'
          '\n6: Dcy (1)'
          '\n7: Lys，Dly (2)'
          '\n8: Lys (1)'
          '\n9: Dly (1)'
          '\n10: Unnatural Amino Acid Supplement Library (193)')
    print("Format example for manually entering collections: (Dal),(Dar),(Das)\n")
    for i in range(datal11):
        print("Please select the set of amino acids for"+"seq%s" % (i+1))
        datal12 = input()
        if datal12 == '1':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col1

        elif datal12 == '2':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col2

        elif datal12 == '3':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col3

        elif datal12 == '4':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col4

        elif datal12 == '5':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col5

        elif datal12 == '6':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col6

        elif datal12 == '7':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col7

        elif datal12 == '8':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col8

        elif datal12 == '9':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col9

        elif datal12 == '10':
            exec("seq%s=[]" % (i+1))
            locals()["temp%s" % (i+1)] = seq_col10

        else:
            list_define = datal12.split(',')
            exec('locals()["temp%s" % (i+1)]=list_define')

    seq_list = []
    for i in range(datal11):
        if i == 0:
            for a in locals()["temp%s" % (i+1)]:
                seq_single_list = []
                seq_single_list.append(a)
                seq_list.append(seq_single_list)
        if i != 0:
            list_ling = []
            for b in seq_list:
                for a1 in locals()["temp%s" % (i+1)]:
                    c = b[:]
                    c.append(a1)
                    list_ling.append(c)
            seq_list = list_ling
    seq_list_end = []
    for seq_e in seq_list:
        seq_list_end.append(''.join(seq_e))

    with open("seq_gene.txt", 'w+',
              encoding='utf-8') as f_target:
        for myadata in seq_list_end:
            f_target.write(str(myadata) + '\n')
    f_target.close()

    print("The sequence is generated successfully, and the sequence file will be split. "
          "Please enter the number of sequences contained in each split file. "
          "If there is no need to split, enter skip\n")
    datal13 = input()

    def split_u(file_name, split_num):

        wdata = []
        count = 0

        for count_all, line in enumerate(open(file_name, 'r')):
            pass
            count_all += 1

        with open(file_name, 'r', encoding='utf8') as f:
            d = f.readline()
            while d:
                if count % split_num == 0 and count != 0:
                    count_new = int(count / split_num)
                    with open("seq_split/"+"sp_" + str(count_new) + ".txt", 'w+', encoding='utf-8') as f_target:
                        for mydata in wdata:
                            f_target.write(mydata)
                        wdata = []
                count += 1
                wdata.append(d)
                d = f.readline()
            if count == count_all:
                if (count % split_num) == 0:
                    count_new = int(count / split_num)
                    with open("seq_split/" + "sp_" + str(count_new) + ".txt", 'w+', encoding='utf-8') as f_target:
                        for mydata in wdata:
                            f_target.write(mydata)
                        wdata = []

                else:
                    count_new = int(count / split_num)
                    with open("seq_split/"+"sp_" + str(count_new + 1) + ".txt", 'w+', encoding='utf-8') as f_target:
                        for mydata in wdata:
                            f_target.write(mydata)
                        wdata = []

    if datal13 == 'skip':
        print("The sequence is saved in seq_gene.txt in the current folder\n")
    else:
        if os.path.exists('seq_split') == False:
            os.mkdir('seq_split')
        else:
            filelist = [f for f in os.listdir('seq_split') if f.endswith(".bak")]
            for f in filelist:
                os.remove(os.path.join('seq_split', f))
        a = split_u("seq_gene.txt", int(datal13))
        print("The sequence is saved in seq_gene.txt in the current folder, and sequence segmentation is performed.")

    print("Do you want to generate the supporting SVL cyclic peptide generation script? "
          "Enter (yes/skip) to (execute/skip)\n")
    datal14 = input()

    if datal14 == 'yes':
        print("Please select the current cyclic peptide type:"
              "\n1.Double-bond stapled peptide based on S51 and S52 amino acids"
              "\n2.Linear peptide"
              "\n3.N- and C-terminally linked cyclic peptides"
              "\n4.Disulfide peptide")
        datal141 = input()
        if datal141 == '1':
            print("Please specify the site number where the S51 amino acid of the stapled peptide is "
                  "located (ACE or NME will not be counted). For example: enter 3 for the site number "
                  "of the third amino acid from left to right.")
            datal1411 = input()
            print("Please specify the site number where the S51 amino acid of the stapled peptide is "
                  "located (ACE or NME will not be counted). For example: enter 3 for the site number "
                  "of the third amino acid from left to right.")
            datal1412 = input()
            print("Does staple peptide add ACE? (yes/no)")
            datal1413 = input()
            print("Does staple peptide add NME? (yes/no)")
            datal1414 = input()

            count_svl = 0
            svldata = []
            with open('sp_svl_code', 'r', encoding='utf8') as f1:
                d1 = f1.readline()
                while d1:
                    count_svl+=1
                    if count_svl == 4:
                        d1 = d1.replace('generate_number', str(datal13))
                    if count_svl == 10 and datal1413 == 'yes':
                        d1 = d1 + "				pro_Acetylate first Residues [];\n"
                        datal1411 = str(int(datal1411)+1)
                        datal1412 = str(int(datal1412) + 1)
                        if datal1414 == 'yes':
                            d1 = d1 + "				pro_Amidate last Residues [];\n"
                    if count_svl == 12:
                        d1 = d1.replace('S51_POSITION',datal1411)
                    if count_svl == 22:
                        d1 = d1.replace('S52_POSITION',datal1412)
                    svldata.append(d1)
                    d1 = f1.readline()


            with open("SVL_S51-S52_generation_script.txt", 'w+', encoding='utf-8') as f_target1:
                for svldata1 in svldata:
                    f_target1.write(svldata1)

            print("The generated SVL script is stored in the current directory\n")

        if datal141 == '2':
            print("Does linear peptide add ACE? (yes/no)")
            datal1413 = input()
            print("Does linear peptide add NME? (yes/no)")
            datal1414 = input()

            count_svl = 0
            svldata = []
            with open('lp_svl_code', 'r', encoding='utf8') as f1:
                d1 = f1.readline()
                while d1:
                    count_svl += 1
                    if count_svl == 4:
                        d1 = d1.replace('generate_number', str(datal13))
                    if count_svl == 10 and datal1413 == 'yes':
                        d1 = d1 + "				pro_Acetylate first Residues [];\n"
                        if datal1414 == 'yes':
                            d1 = d1 + "				pro_Amidate last Residues [];\n"
                    svldata.append(d1)
                    d1 = f1.readline()


            with open("SVL_linear_generation_script.txt", 'w+', encoding='utf-8') as f_target1:
                for svldata1 in svldata:
                    f_target1.write(svldata1)

            print("The generated SVL script is stored in the current directory\n")

        if datal141 == '3':
            count_svl = 0
            svldata = []
            with open('ncp_svl_code', 'r', encoding='utf8') as f1:
                d1 = f1.readline()
                while d1:
                    count_svl += 1
                    if count_svl == 4:
                        d1 = d1.replace('generate_number', str(datal13))
                    svldata.append(d1)
                    d1 = f1.readline()

            with open("SVL_NC_generation_script.txt", 'w+', encoding='utf-8') as f_target1:
                for svldata1 in svldata:
                    f_target1.write(svldata1)

            print("The generated SVL script is stored in the current directory\n")

        if datal141 == '4':
            print("Does disulfide peptide add ACE? (yes/no)")
            datal1413 = input()
            print("Does disulfide peptide add NME? (yes/no)")
            datal1414 = input()

            count_svl = 0
            svldata = []
            with open('ssp_svl_code', 'r', encoding='utf8') as f1:
                d1 = f1.readline()
                while d1:
                    count_svl += 1
                    if count_svl == 4:
                        d1 = d1.replace('generate_number', str(datal13))
                    if count_svl == 10 and datal1413 == 'yes':
                        d1 = d1 + "				pro_Acetylate first Residues [];\n"
                        if datal1414 == 'yes':
                            d1 = d1 + "				pro_Amidate last Residues [];\n"
                    svldata.append(d1)
                    d1 = f1.readline()


            with open("SVL_disulfide_generation_script.txt", 'w+', encoding='utf-8') as f_target1:
                for svldata1 in svldata:
                    f_target1.write(svldata1)

            print("The generated SVL script is stored in the current directory\n")

    print("Press any key to continue to the next generation")
    data_end = input()
