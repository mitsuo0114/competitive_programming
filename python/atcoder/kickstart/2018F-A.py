sample_input = """
6
3
ABB
BAB
3
BAB
ABB
6
CATYYY
XXXTAC
9
SUBXXXXXX
SUBBUSUSB
4
AAAA
AAAA
19
PLEASEHELPIMTRAPPED
INAKICKSTARTFACTORY
"""

small_input = """
100
3
ABB
BAB
3
BAB
ABB
4
AAAA
AAAA
50
ABBBBBAAABBAABBABAAABABAAAAABBBBAABABAAABABAAAAABA
BBAABBBABBBBABABABBAABABABABAAABAAABABBBBBBBAAAAAA
50
BBBBBAABBBBABBBAABBABABAAABBBABABBBAABAAABBBBBBBAA
AABAAAAAABBBBBAAABBBBABBBBABBAABBBBBBBAABBBAABABBA
50
AABABBBABAAABBBABABABBBBABAAAAABAABAABAABABABBAAAB
BBAAABABAABBBBBAAABAABBAAABBAAABBBBABBBABABABBABAA
50
BBAABBBBAABAAAAAABABABABABABABABBAAAABABAAABBAAAAB
AABAABBAAAAAAABBAAABABBAABBABBAABBBBABBBBBABABABAB
50
BAAAAABBBBABBABBBAAABAAAABBABBBBBBBAAAABABBBBAAABA
BABBABBAABABBBAAABAAAAAABAAABBBAAAAAABBBABBAABABAA
50
BAABBBBABBBABABBABBAABABABAABBBAABBABAABBAAABBBBAB
BABBBBAAABAABBAABAAABAAAAAAABABAAABBBAABAABBBABBAA
50
AABABAAAABAABBABBBBAABBAAABAAAAAAAAABAAABAABABAABA
BBABABAABABABBBAABBAABABBBAABBAAAAAABAAABBBBBAAAAA
50
BAABBBABAABBABBAAAABBBABABABBAAABBABAABABABBBAAABB
ABBAABBAAABBABBBBAABBAABABBABBABBBBBAAABBABBABABAB
50
ABAAABAABBAABABABABABBAABBAABBAAAAAAAABAABBBBBBBAA
AAAAAAAAABBBBABAAABAABBBAABBAAAABBAABBABAAABAAABBB
50
BBBAABAABABBAAAAABBABBABBABABABABBBAABABBBBBABABAB
BBABBAAAABAABAABBBBBAAAABBBAAABBBABABABBABBBBBBBBA
50
BBBABBBAABBBBBBBBBABBBBBAABABAABBAABABABBAAAAAAAAA
AABBAABAAAABABAABBAAABBABABAAAABAAAAAABBBBABBAABAA
50
BBAABBABAAABABBAABABBBBBABBBAAAABBAAABAAAABABABAAB
BABAAAABAAAAAAAAABABBABBBABABAAAAAAABBAABABBBABAAA
50
AABBAABABBBAABABBBAABAAABAABABBBAAABBBBBBAABAABBAB
BABABABBAABBAAAABAABBABBABBBAAABAABABBAAABBBABABBA
50
AAABBBBAABAAAABBBBAABBBBBABBBAAABABAAABABAABABBBBB
BAABAAABABBABAAAABAAAABAAABAABABABBBBBBABBBABAABBB
50
BABAABBBAABAAABABBAAAABAAAABABBAAAABBBBBBBBABABBAB
ABBBBBABBAABABBAAAAAABBABABBBAAABABAABBBABBAABABAA
50
ABAABBBAAABBBABAAABAAAAABBBBAABBBBBABAABAAAAABAABB
AAAABAAAABBABABABABABAAAABBBAAABBAABBBABBAAAAABABB
50
BBABABABABBBAABBBAAABAAAABABBBAAAABAABABBBBBAABABA
ABABBABBBABABABABBBBABBAAABABBAAAAABBBBBABABBAAAAA
50
BBABBAABBABABBAAABBAAABABABABAAAAAAAAAABABABBBBAAB
ABABAABABBABABAAAAABABBABAAABAABAABAAABBAABBBBBBAA
50
BABBBBABABAAAAAABAABBBBAAAABBAAABAABBBBAAABBBABABB
ABBAAAABABBBABAAABABBABBBBAAAABAAAAABBBAABBBAAABAA
50
AAABBBAAAAAAAABBAAAAAABBBAABAAAAABBBAABAAAABABAABA
BAAABABBBABBABBAABBABAABBBBBBBBABBAABAAAABBBAABABB
50
BBBABAAABABBABAABBABAABABAABBAABAAABAAABBAAABBBBAB
BABAAABBABAABBAAAABABABABBBABAABAABABAAABAABABAABB
50
BBBBBABAAAAABAABABABBABBBABBBAABAABBBAABBBABBABABB
ABAAAAABBBBAAABBAAAABABBAABABAAAAAAAAABAAAAABAABAB
50
BBAABBBBAAAABAABBBBAAAAAAABABBABBBBAAABBBAABAABBAA
ABAAAAABABAABABBAAABABAAABAABBBAAABBABABABAABBABAA
50
BAAAABBAAABABABBBBBBBBAABABBABBBABAABBAAAABBABABAA
BABBABABBAABBABBABAAAAAABBAABBBBAABAABABBABAAABABB
50
ABAAABABBABBABABBABBABAAAAAABBABAABBAABAAABBAABBBA
BBBBABAABBABBABAAABBBBABBBBAAAABAAABABAABAABAAABAB
50
ABBBAABAABAAABABAABAAABBAABABAABBABBABBBAAAABAABBB
ABBBAABBABABABBAABABBBBAABBAAAABBAABBABBBBAABABAAA
50
BBABBBBBAABABABAABABBABAAAAAAAABABBAAABBAAABAABBAA
BBABBAABBABABABBBAAABBAABBBBABAAAABBBBABBAABAABBAB
50
AABBBAABABBAAABBBBAAABBBAABBBBAABBBAAABBBABABBABAA
AAAABABABBABBBABABABBBBBBABABBBAABBBBABAAAAABBAABB
50
BAABABBABBABABBBAAABABBABABABAABBBBBAABABBBBBABBAB
ABBABAAABABBAAAAABAAABBBBAABBABABBAABAABAABAABABAA
50
BABABBBABBABAAABAAAAAABBBABAABBAABAABAABABAABABAAB
BBAABBAAABAABAABBAAABAAAAABBBBAABAABABBAAABABAABAA
50
BBBAAAABBBBBAAABAAAAABABBAABBABABABAABAABAAAABAAAA
BBABABABABBBABBBBBAAABABABBBABBBABBABAAAABAAAAAABB
50
ABABAAAAABABABBBBBAAAAABABABABAABBAABBAABBAAAAAABB
AABABABBABBABABAAABABAAABBBBBAAABAABBAABABBAAAAAAB
50
BBBAABBABAABAAAABBAAAAABBABBBABAABAABABBAAAAABBABA
BAAAAAABABBBBAAABAABAAABABBAABAAABABABBBABABBBBBBA
50
AAABBABABAAAABAABABBABAABBBBBAABBABAAABABABBABBABA
BAAAAAAAABABBAAABBABBABABABBABBBBBBAAAABBAABBAABAA
50
AAABAABABBABAAAAAAAABABBBBAABBABAAAAABBABBBBBABAAA
ABABAABAAABBBAAAAABBABBABBBABAABAAAAABAABABBBBAABA
50
AAABBBBAAABABAAAAAABAABAABBABABBBBBAABAAAABABBAAAB
AABAABAAAABBBAAAABAAAAABBABBBBAABBBBBABBAAAABAABBA
50
AAAAAABAAAAAABAAABBABBABABABAABABBAAAABAAABBAAABAB
BBBBBBBABBBAABBBAABABBAABBBABBABBAABABBBBBBAABBAAA
50
BBAAABBABBBABAAABAABAAAAABBABBAABBBABBBAABABABABAB
ABBAABBBBABBBBBAAABAABBABABAAAAABABBABAAAAAABBAABA
50
AAABBABBBBBBBAABABAAABAAABABBBBAABBABABABBBABBBAAB
AABBBBBABBAABBBABABBBABBBBBAAABBABABBABABABAABBABB
50
AABBAABAABBBAAABABAAAABBBABAABBBBBABBBAABBBBAABABB
ABABABABBAAAABABABBABAAAABABAABBBAAABBBBBAAABABAAB
50
BBAAABBAAAABAAABABAAAABABBAAABBBBABAABAAAABAAAAAAA
BBBAAAABABAABBAAAABBBABAABAABBABAAAAAAAAABBABABBAB
50
BABABABABABBBABBAABABBBBABAAABBBBABBBABBBAABABBABB
ABBBBAAAAABAAABBBBBBBABBBBBABAAAAAABAABAABBABAAABB
50
ABAABBBAABBABBBABABABAABBBABAAABBABBAAAABABBBBAABA
BAAAAABBABAAAABBBBAABABBBBABABAABBAABABBABBABABBBB
50
BAAABAABBBABABBAABAABBBABBBBBBBBBAAABAAABABBBBABBB
AABBBBBBBAABAABBBBBAABABAABBABBAABAABAABAAAABABABB
50
BBBAAAABBBAABBAABAAABAAAAABBBBBBBBBBABABBBAAABABBA
ABBAAABBABAAAAAAAAABBBBBBBBBBBBAABAAAAAABABABAAABB
50
BAAABAABBAABBBABABABAABBABAABBBABABBABABAABBAAAAAB
BBAAABBABBBBBBBAAAAABAAABBABABAAABBABBBBAAAAABBBBA
50
BAABABBAAABBBBBBABBAABBBBBBABABBABBAABBABABABBBBBB
BABBBBBBAAABBBAABBAABABAAAABBAABABBBABABBBABABABBA
50
ABBABAAAABBBABBABAABBBABAABAAABBAAAAABBBBAAAAAABAA
BBAAAABABAAAABBBBBBAABBBBBBBBAAABABAABAAABBAAABAAA
50
ABBAABAABABAABAAAAABBABABAABABBABAAAAABABAAABBBBBA
BAAABBAABBABABABABAABABBAAAABAAAAAABABBBBBBABAAAAB
50
BAABBBAABBABBBABBABBAAABABABAABAAABBABBBBABABABAAB
ABBBAAAAABABABBBAAAABABABBBABAABBAAABBBABAAABAAABA
50
BBBBBABABAABAAABAABBAAAABAAABBABABBBABBABBAABBAAAA
BBBBBAAABBBABAAABBBAAAAABAABBBBBBBBBBBABBAAABABABA
50
BBBAABBBBAABABBBABBBBBABBBBAAABAABBBBAABBABBBBBABA
BAAAABAABBBAAABAAABABABBABBBBBAABABBABBBABABABAAAA
50
BBABABAABBBAABBBBBBAABBBABAAAAABBABBABBAAABBBAABBA
ABABBABBBBABAABBBAAAAABAAABAABBBBBBBAABABABAABABAA
50
ABBABBBBBBABABABBBBABAABAABAAAAAAAAAAABAABBABAAABA
ABAABBBAAABBBABABAABBBBABAAABABBAAAABBABABAABBBBAB
50
ABABBBAAAAAAABBBAAAAAAABBABABABAAAAAAAABABBABBABBB
BBAABABABAABABAABBABABBABAABAABBBAABAAAAABBABAABAA
50
BABABABBBAABBBABABBBBBABBBAABAABABABBABABABAAABBAB
ABBAABAAAABBAAABBAAABBBABBAAABABBAAAABAABAAAABBAAA
50
AABBAABBABABBABABBABBBAAABBABAAABBABBBBABAAAABABAA
AABBBABABBABABAABAABAAABBAABABABABAAABABBBBBAAAAAA
50
BAAAAAAABABABBABBABBBABBBAABBBBBABAABAABAABABABBAB
BAABBAABBAAAAABBABABAAABABAAAABBBBABABABABBBABBBBB
50
BBAAAAAABBAABAAAAABBABAABBABBBAABBAABABBAAAABBAABB
ABAABBBBAAAAABABBAAAAAABBAABBAABBBAABABBBAAABBAAAB
50
AABBAABAABABBABAABBBABBBAABBBBBABBAAAAABAABBAABABB
BABAAABABBABBABBBBBAAAAAAAABABBBAABBBABBAAAAAABBBA
50
BBBBABBAAAAABBAABBBBBABAABBAABBAAABBAABBBABBABAABB
AAAAAABAABAABABAAAABAAABAAAABAAABBAABBBABBAABBBBAA
50
BBBAAAAABAAABBBAABAABABBAAAAAABBAAABBBBBBBBABABAAA
BBBBBABABBBBBABBABBABAABBBBBBAABBAAABBABABBBABBABB
50
ABBABAAAABBAAAABABABAAAAAABBBABBBAAAABBABAABBAAAAA
BBBABBABABBABAAABBBBBBAAAAAAABAAAAAAAABBBBBABBABAA
50
AAABBBBAABABAAAABABBBAAABBBABBBABAABABABBAABBBBBBB
ABBABABBBBAAAAABAABABAABBABAAAAAAAAAABAABBBABBAAAB
50
ABBAABAAAABABBBABBBBBABBBABBBBAAABAABBAAABBABBAABB
BBAABAABBAAABBBAABBBAAAABBBBAABBABAAAAAABBBBBBBABA
50
AABBAABABAAAAAABABBAAABBABAAABBAAAABBAABBBBBAAABBB
BAAAAABBAABABAAAABBAAABBABABBBABBAAABBABABBABAABAA
50
ABAABABABBABBABBAAAABBBBBBABBABABAABAABABABBAABBBA
ABABABABAAABABABBABABBBBAAABAABBABBBBABAAABBBBABBA
50
BAAABBAAABBAABABBBABAABBBBBBAABBAAABBBBABABBAAAAAB
AABBBBBBBBBAAABABAAABBBAAABABBABBBABBABAABBBABBBBA
50
BBABBBBBBABBBAAAABBBABABBBBAAAABBBBBBBBBBAABABABBB
ABBABBBBABBAAAABAAAABBBBAAAAABABAAABBABBABBABBAAAA
50
ABBBAAAABAABBABBABBBAAAABBBABABABBBAAABAABABABABBA
BBAABAAAAABAAAAABAAAABAABBAABBABABBBBAAABABABBBBAA
50
ABAAABBBBAABAABAABBBABBABAABAABABBABABAABBBBBABAAA
ABABBAABBBABABBAAABBBBAAAABAAABAAABBAAAABABAAAAABB
50
ABBAAABBBABBBAABABABBBABBBBBBBAABAAAABAABABBAABAAB
ABAAAABBBBBBAAABBABBBBBBAABABBABAAABBAABAAABABBBAB
50
AABAABBBABBBABBBBBBBAAABBAABABAAABBAAAABBAAABBABBB
AAAAAAABBABABAAAAAABBBAAABBBBAAABAABAAAABBABBBABBA
50
AAABABBBABABBAAAAAAAABBBAABAABBBBBBABBAABAAABAABAB
BBAABABABBAABABBBAABBBBBAABAABBAABAAABBBBBAAABABBB
50
ABABAABABABBBAABAAABAABABBBBBAABABAAAABBBAAABAAABB
ABBBAAABABBAABAABAABBAAAABBBBABAAAAABBABBAAAABABBB
50
AAAAABABBABABBAAAABBBBBBAABBBAAAAAABAABBABABBAABBA
AABABBAAAABAABBBBBBBBBBBBBBABBBBBABBAABABBBBABABBB
50
BABBAAABAABBBBABAAABAABAAABABABABAAAAABBBAABABABBA
ABABAAAABBBBABAAAABAABABABABABBAABBAABAAABBBABAABB
50
BBAABBAABAAABAAAABBBABBBAABBAABBBAABBBBAABBBBBAABB
AABABABBBBBAABBBAAAAAAABABABABAAAABABABABAABABAABA
50
ABAABABBBBBBBBAAAABBBABAAAAAABABABAAABABAABBBBAAAB
ABABABBBAABBBBABAAABAAAAAABAAAABAABBBBBBAAAAAABBAB
50
BAAAAAAABAAAAABBBBBAAAAABABBBABBBABBAAAAABAABABAAA
BABABBBABABBAAABAAAABBBAABAAAABBABAABBABBBABBAABAB
50
AAAABBBABBABBBABAABABAABBAAAABBAABAABBABABAABABBBA
BAABAABAABBBBBAABBBBBBBABBBBABAABAAAABABBBABABBABA
50
ABBAABAAABABBAABABAAAABABBBBABBAABABBBBABABAABAABA
BBBBBABBAABBAABAABABABBAAAAABBABABBBAAAABAABABBABA
50
BAABBBABBBAABBAAABBAAAAABAABABBBBBABABBBBAAABAAABA
BAABBBABAABABAABABABAAAAAABBBAABBAAABBAAAAABABBAAA
50
ABAABABABBABABBBBABBBABAAAABAAAAABAABAAAAAAABBABBB
AABAAAABBABBAAABBBABABBBBBABAAAAABBAAAAABABAAAABAA
50
ABBBAABABBAABAABABBBABABBAAABAAAAAAAABBAAAAAAABBAA
BABABBBBBABABBBBBBABAABAAAABBBAAABBABAABABAAABBBBA
50
BAABAAAABBBBBBBABABBBBBBAAABABABBBBBABABAAABBAAABB
BAABAAABBABBAABBBABABBAABBAABABBAABBAABBBABABABABA
50
ABABAABBAAABABAABBAAAABABABBBABBBAABABBABABBBBAABB
BABABBABBBBABABBAABAAAAAAAABBABBAAABAABAABABABAABB
50
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
50
BBBBABAAAABBABBBBBBBABBBBBBBAAAABBBABBBBABBABABBBB
BABAABBAAAAABABBBAABBAABBBAABAABABBABBAABBBBBAAAAB
50
BBBAABBAABABABBBABBAABAABABAABBBABBBBABBBABBAABBBA
ABBBBBAABABBAABABAAABABBAABAAAAAAABBBBBABBABBBABBA
50
BBBBBAAABBBAABBBAABBBABBBBAABBABBBAABBBBBBBBBABAAB
BABAABBABBAAAABBABAABAAABBBABABABAAABBAABABBABBBAB
50
BAABBBAAAAAAABABAABAAAAABBBAABBBBBAABBBAAAAABBABBB
ABBABBBBAAAABBAABABBAAAAAABBBBBAAAAABBABBAABBAABAA
50
ABBBAABBBBBAABAAABAAAABAABAABBAABABAAAAAAABAABBBBB
BBAAABBBBBABBAABBBABBAAABBBBABAAAABBBBABBBABBBBABA
50
AABABBBAABAABABABABABBAAAABBBBABAAABAABBBBBAABAAAA
BAABBBABBAAABBAABAABBABBAAABAABBBABBAAABBBABBBBBAB
50
BAAABAABBBAABABAABBBAAAABBAABABAAAABBBAAABABBAABBB
ABBBBBBABAAABBBAAAABBBAAAABAAABABBBBABABABBBBABAAB
50
BBBABABAAAAABABABBAABBAAABAAAABABABABABAAABAABBBBB
AABAAAAABBABABABBBBABBAABBBAABAABBABBBABAABAAABABA
1
A
A
"""

large_input= """
100
3
ABB
BAB
3
BAB
ABB
6
CATYYY
XXXTAC
9
SUBXXXXXX
SUBBUSUSB
4
AAAA
AAAA
19
PLEASEHELPIMTRAPPED
INAKICKSTARTFACTORY
50
YOKSNOGKIFDBBLHIMFMCMRBPLNCQLOBIJEERMLAEMQKILOFOXZ
ZEOPBIMKNBLOHOBGQLMLFROXMJDLNKLIEMIAKFCFXQSIERMBCY
50
YRJERRDRIGDJSQNGPKRRDIBHOEEAKDLEFNHERDBBMDJEKGARXZ
ZJERJBXDDDERNPDHRKMDAIKRELFNEDKGABOJHRBRRIGSGEQEXY
50
XTWKVTBJKYTXGTXWPPHSMTJQGISJSCWVTFCTDAHTIIQFWRVVNJ
EOJOCJBHYTSKIHQLGGVNEOQUMBCPAOXKHREIXIHZZGKIMRURYE
50
YJJRQISDFHECNOQMJJDQQFAICPDNOEGSJNGACAFHFFCQGBAJXZ
ZJQOGFSEGQCCPDJFFBAHJCDQNNQOCQXFGMDIJXFHAJSIAEARNY
50
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
MZMBVNVRMJHJAXLSYLMADIFXOBKXWHFQYTBEWKXVUEMFQOBDFN
50
EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
YIKWUBJXRIFAIFNYIYDSADJNASAIHEQUPNFVATHTMZPNMXZPYO
50
YJACUWYKMSFKVVZITYHIUZINXKBWRFXFPVFLJUZDIAYHTHOKZK
JEMFKGHDARGNJOQNSIFYCXKYCGXMXOEOANILDEFZBPTFVFIEZF
50
UAAEKDCZOULRZGJTCYAMLAJRPUDEAJDBALUOJIGLEDTYSAGPBE
DHCUUQDFSLIAHPAZJCRJTEJIXDTYRLNTDZNDBTPITHEPRYSQVV
50
MNBLHDELTPRNFNPICXKJLCUUYGCXLXQIKBUVZUKEINRTIARVTQ
DBVOVCHCWSPHTINWAQFEDGJIQJNHVWJVPPCXAZCTYOZPRHQKZQ
50
FAGCKBGLYXVRWBVUDOKMTLJCGCOTYXIYPJVZRICKPMCCJQUGQY
TZYQUCGCDXCNXSPLCMZGTMYOLYPADVBVVQBHCQIGIFBCXIFHSO
50
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
BOCXLOBNNHKMDREQCQNMSAHDFQGWMGWSYIIFNNVOVFCLZFNDAY
50
YDSRNCQQPKELGQSLDNJKHFBAGLFLAQKAANKGDGKDDIEKENFDXZ
ZINRLGANGDXEDQCSLPSLKGEXEBKKJFGDNAAKDKFDQQFQHNALKY
50
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
JXUMJLOOEOEKBBBBELLYWWPVWXVWNOVLBYJGBLJMRAXBSIJCYY
50
YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
SAODHMVNFYDBVPDMFMNIPDTFYTOIPHHNICTHULGDRHKRIVEISP
50
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
FSGQBDCLWQRTCOECHGNHMNDSINIPLXVELQSMHTCJHUYUHSADTP
50
YKMHHANJSBNEQOMIBKJPKBNFHDPHIEFGCSBJIJRDHKLQROKKXZ
ZRIBCESHJMPNRAHKBDOQIKHXHXMENKKJFQLGJPBOIJSDKBFNHY
50
KPKOCDKNBNRQZTJGGIGJYJJXGQWLSOMUDSTZGJHRLUSBNGNMZC
IXZQPXKJOEYYWPQHTVIZCSWAZADEUCZXBBDBJUIGJWWYWCIYYH
50
OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
XMAIQWJDRRMXCXDUMVDFNJNVLLEMOIFEDLGVITZOQZVAODAKJX
50
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
DIWSWZYGZQAJZUPDXFNURHTYUTTJKIZYGYDRPHWDRFXFFTUHUN
50
LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
EQQTXJFEIDZBFKPUWQNVRJQVRSSIZDKMJHETKBYJMWOIVICFYS
50
TQTIFUJHJMJZOAODFXLFKKMTUVZJGWLIMDTRVWLGNYNUOKYXZD
DHYFSJHDPLWJJZMWYNSTVJETDECXBQWBVKLLHOKBKKNHDJZBHP
50
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
IWVQSULPTAFXDSPBBCLEGTZBZBYUYDFIRLRGBTYRFNOIFVJUDK
50
YGGDBLCOBPPPDMBELMBDBRSMBRGAGKEDALEARBDINHKNIKSGXZ
ZXEMMBCKPSBLXGLHPSLARNBIMPNDRDGBBGABEGRAKDEIDKBODY
50
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
NDSNISFRRBLSRGXSCOIBBCAFVPKHPUYXGETFIRIWXKVAMIYGZN
50
RSSSYIJLLPWMBRQKMXBCCSIQWNGLMKJDHUYQLKGJGGIZXMOEQI
XLDIEBDLJVDUOKWOASZQUSIEXLRBTBMNEXLKNSBUETRCPDEXCB
50
CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
ALVIMQPHGLGMKEPODHLOKOWEHTRESPCBQNTQASXZTREYBOJOKY
50
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
VESLBSYDVWLIBIZVCWEMRJHHPTVGYESKYHKETVHKTIXYIVYXMY
50
GJLRIXJOOOHZBNYYNTYBVLQQZPJOMYJAHMGDNBIQZNVCEDFOOM
BMQLIONWPFKLOTQISKSWAYSIBEASBOSPBWFIHYGOWFVZPYMMGH
50
YIICJCESJOCGFOABCPINBNLAPNJRMIGMGRODQNSCNHPCMBCIXZ
ZDNGPJBMIBQONCLIBNXGCCEONXSRIPACCJCSMOGNPFCHJARIMY
50
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
KTOLXVVZGLMKQZDIUKNXKFHDBFUOXUOCFFAJXWFWYDASTIJXCA
50
CLCLDKWGCDRNTQWKBMHIORBARVLQHLLXIOVCHRBPVVYTKUOVAM
FETPBBGUMEJKVBVMOHJRUBSDHGMSBCCLKGLBDVKXPJWUOBVMNL
1
A
A
50
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
ZOIBUOKKFXHAZIDXNMMHULBCHKQXVOECVKLVASSILHUAXLCVMM
50
YOJAINKEPFAYDYIXDKXVFHDWVRQHLFWEVLACLFGQCBZMDVRCYK
OXRZSCGOFBBDUANNLEIVFBYCHPIJAASQWEJFGZGJJLDWPERYRO
50
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
GNELGBIUGQIHPHPTFLDTBQMIFVKBVWPGLMRPMXAVASEIXZMNLA
50
YGCHSDOASDIMAABLQINKNNHOHQGPECRAPPNCBIIIPHNBMORGXZ
ZNHIADKXHPHRRQMOBPCAIPSNGBOMELIANCPNXSGNAIBDHOQICY
50
QDWNJHYHIWBJUECZCUCKDSBVKFRUEGKPCYBKZRAGBAVDWDOTTI
QPOFAWFYWHZIQTXXAAOOVHNEUTJQQRSGSIQVBKTGDJCEDHCROC
50
YDBNFFGJMFGDISNGMDLEOCMQMHMJMONHJCNHOBQQPFPKMEPDXZ
ZFMMHPBGBNEQDMFPKSOMNCNMQIGFNHDJXDFHPLGMOQJXOJEMCY
50
MBVWLTZTIRJKUMADPFQHMUUHOCFJJRNCHMLOMUFUDMKGDBSYVE
VWXJBBGRQMZHDWSHIFLKTONGTYFWGSUFRDCETYTVURFCILGJGP
50
YJHHSQLLOSRAIJKLRNRBORCFPQKBSKGHENPSSERDGFASJKKJXZ
ZRHKAHXSQRGRPBASLRISEOKSQBXJJJSDNLFLHOKSPEFNKKRGCY
50
JMRDRJCQGCIVQCJIUEEMPRZDFEDCQBJAQORLDOKJRDXXIDHHMC
SOLKDYVNXSSYWFWEPBFBUOPVXEWHTRWNSAPVFWOIOBIZPZYUPD
50
LDHDSGPBXLXLLOKPGDZMKWCKOYQGJIRUUESBFKSLIEFHYTRXMK
WOXPQEQFKSJBKBHWGHTQMEIKQELFKVPIRDPIYJUMPIDFMYSXAF
50
ILTNEJXGSRHWYGWHTOXQXHBXGPRADDVQPSNVDWXJFVRXOVYJZF
SPAPSDLNZFOCOCSYSZWNPDPYOUSUCEMXPQEISYCFOJOGFFKSQK
50
WCMKCGOSSMETXXCJHSJCGXBFYBVATUAZIUNNVDTTPKUHGMDSEM
IFGZJKPDKEHJBETQJNYXKCYAAEJWTHNWBDANSNGNAPSZZZAUKJ
50
YIPTCHZFCAAVZRBAOKYYJSHBPXYADWVCOWTJNMRHRBBRQVCVMC
LOZDVTJJBFVCTUVTMCTFWDLCCJRVLSHJAHRRRRMBWGTWTVJVMP
50
YHHLFAOEMRRQGABEKPMOOIJDNICGGBQDRNBBOMBSERAJDFLHXZ
ZLABHEDBNABNXDSEIQOPGRDMEMHOKRJFICXRBFLGBQOJROMGAY
50
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
KHLIABRBIYADWHVFAHIQIIFXBCIEYBJAPZJMNVVFNYMHZTPWII
50
AOCUQSOZQKXPXERJKTXUFMYIPXRGUGLCVPSDQBWHYWOUGSHIEB
CVEJOIIXKEOAVFPZBFKQWXFKHPDPHGZTZZNEHGYIFSXGCAVZKC
50
YHCHSADSALLRLOOONDEAHKSPIKBBCBHBMAKGOJEAQILCHMRHXZ
ZCLKXHLABHEBCIHOKBDAMSQALJIEMSOARRAXHPLNSHOKGBCDOY
50
GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
QBIUHJOIATYRTOLITYTNUXYIZPVQBXAHPKHGFUIUQNEVIVTKOI
50
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
XSJLUTRJUNTYMOBOLOYMEWKNEVEUGEBYEEJSLONWVTSRDHCHGJ
50
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
KJTXRWQYXQTDKFULQIEAYPTKICUJWXEVUYCXZGYAIRZPAVRYOC
50
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
HYHXKZJYFBDSGVLZWLUKSXRNMFBPMKSOJQONXHWBCFYPOVGTUL
50
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
50
LTFHUGOTGCGROUEODZZDCPXLYDKCFOWXFSOHVHKNSQMOJBRJCF
SWJFKFHZXVSMFEBJLYEIOUBLFBUKNDMGHUYTZVSMGNUYVVYRWF
50
YLCFHCQJSAADSDQKBDKRKFJOSOSPCPCJARNOGDBDKMLFCDALXZ
ZMKCCOJCKQNSCDLAJFDQDOCAKRGXAFPSPKBDDSSOAJBDRFXHLY
50
YBQLPAKPQAFOLNQJGDNEIGPDAEFQGGSFESPADODJIEFBFEDBXZ
ZFEFEIPFNXSKDQEDSDOJBGFDGQQALAXAGNFGQPDPAPLIEBJEOY
50
JZYRXNYRCERRSIBVMPVJYOAMYOELNBADXMBKFXWQCUSZBGSPFC
RTWFBTYVTMKUOPYNAASWCIQHNAUNOTSBAOSSGHKKDIDXGVDNJU
50
JCEQPGIAJIWHNDHBCRDFNQOLPVYLHWWNOVZUVNDTTPXTJIQCOF
GZZLCSGYLZNHEFJKEGEBBCNRAGQFFMJQBQBIOOJEFVVCVLTKMD
50
IGGBBKUNDLVKZRVBVFLMQWBTKPKIUSSBBXVOVUOBHXOQERCJDB
IWRANQIVPJCJWTVKLQXMLYJNZAOVVUAXGHPUNAAEIHTKIDZFIP
50
YLJFSHDEDPKJNOSHJKINKIPFNEJIKLPFCSNNEIBMHDIEQAPLXZ
ZJSAKQEIHFSDISNCDIOEMNBJLEKLPEPDIHXJINJXPFKNFKNHPY
50
YRIRDPFBFPBFRNMOPAEJGCDFDPOCLEMHSKKNBJLBFPPLEIJRXZ
ZKCLPRHISJBLJNOIFNOFBFBEPRKCBEXPFAXRDMEDPMPLFPGDJY
50
YHERDLSFADHANKMKRCLARNIGHAGREDPNSFGLSHMSMFLRGRNHXZ
ZRDGNMDHXAGKNLSGAPMRFSLRRXCRIMHFAENLHFHSRANDEGKSLY
50
YEABAHASSCNHIMFBOLMIPQOBQJMQLLLJJIOPACOHRGADONFEXZ
ZNBCIMOLGOXOABALQBJAXODNIQLMAHSPPIJAOFSJCHHMERLQFY
50
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
HVTHLPUVVFYXZNXGJLYBFOVCZCTGDFCDZHNWAXGLACAEPVCBYL
50
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
EENIYGPQJYSETAOGGJOKWFIHWYYVYEGBPCBUTAFQIOOAHKHDFN
50
YARDJODHLGQLKKEGSPIGCERRBERNJSQKNEDRIMEDHKJMEDRAXZ
ZBKXSESLXJDEHGMJECIRRHPDQDDIOERLKDNJNRMKAGRKREGEQY
50
GHNRWTOLYSGCHJYCATUFAGPHQQOHBVEIQINCZKXKUPGJHDOUWW
DRFFINIDNRQOWKLZCLDKWCINRRLZOGMJUTCDXDAOZDVYFIHXGJ
50
YAKAGLDDALMEBLANHEOQEOQANNPECEFNFIKMJCMJQFFJLCPAXZ
ZANLMQXLNMEKEFPEOABCNPLKLGJHDFEECQAXOJCIJFQNFDMAAY
50
HZOMBNPQAZPCJBMGTARNJFINQMTAXFBGANMHQJUSGQFMRUZQNK
BPPDTECIQCSFSRJPUJZBPIEBJCCHHXAYSCBJXZEOWKNAPCUSAO
50
UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
HAWZNRPQXJKTKMVRSUZFGUMTHHNPLNYFBVCHUKGTDCHMVCYHQU
50
IVVDAGTRIPHWUQJWRFOZCOTBDXEAGASJRQNAZYSPSCSXTISYVX
EJEVEIXZHIAYXJRXAJTTORKGRAMSRHJLRQPDKUUOCELCQQYTHK
50
YDRCSSESPEOCCDDFEPJDLGBPREIKIEIONBCQPNBNMRKHKEIDXZ
ZEDKCPIQBPEIODCICERFMDXHEOSECNRKKPLXDPIJSBNNSGEBRY
50
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
VVQNPHBEWNYJPKHJWRXMIADIXHHSYQSQPTXSYZEQVLHBPDYDYK
50
ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
VIYDFATGQTEVZKSWYSQFGAKIBLMSHSVUAMPOYFZRKLBIBEUWQD
50
YEBHAHIEGGOJQRCLAGAMIHRMNCARNHBDIORJFLNDLFEHJCAEXZ
ZFXRHAICQIGNOGEAEHNJLMAHBRGLOAJCHJBICDDRLMFNEHXRAY
50
YLMDEGENIIKFRMNPPCIQBQAANJMNJOOPDMBOAPCNRLRBOJBLXZ
ZENAORXFKPONRDQIOBLQAMBJOIEXNRMBILCJABPGNDMPNMJPCY
50
YLDREJDGMGBAABCPMNGFDLEGKRQJHQGQFFOPMBIFHNNFIKCLXZ
ZRONJENDECJGGGBAGBRPLXAQGBHXFPDQCMFFKFLNIKHIDMMQFY
50
PDATSRRAXDJJALWZEHONDERERDDCCVIKQWFUSPSJDOVCHAYKBI
FFELKBYDGHTKMTGVMLQJYTDRDUCCWDWCPQOLEZXEMQGWSUMAVR
50
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
JNSEOCXTUYGIDLCZIFQEYDLNUJUELJALMICJAPCJRYPIRUIHKS
50
YHMPPLQFERGHLQECQGFDQRNRMECAREOSSBROLIFPEBOJHCQHXZ
ZOQCSHJGEPDFOSXEXRQMEMRQEBQLNRRRCFFQICLPAOEHHBPLGY
50
YOMGBPCGNKRNMPHQMECNAFHQCHKDOMJICRFJFSRGEOJNPQCOXZ
ZNCJXMCJRNFOJCHCNMMDKHXGOGCRFSEQFNKGQBPAEIRMHPPOQY
50
YKFDDKFSQRSHJELHMPRRDMEERDDCNINRLCPCOPFFABDDIEJKXZ
ZLDOIMFDPARNPCRPMHDICBSEDDEJFDRERRNFSXLXEQKKJDFCHY
50
IWMAYJHANXJMUSQZPUHLXZRSZKCNTQPHTPSKETRBYLZDBEVUZH
UCVTVHDOGKENUSPYZWGDJLQLLDEELTWYXUDHDYOTZITQVTGUNB
50
VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
DCYMPNKIJMSHCUROQWUOPRYTQPRCVXRPVEWVECSMOWZVFWLZVN
50
YAHCMJFHELJJKPSHBIIDECOODLDPHCIJDIKQNDBANSMKHEJAXZ
ZOJMFDSJDCDKJKQEHIMOHXHCLDBAHACHSXEINBNELIJJKDIPPY
50
DYYWYBSTVDPJULYOBXFKSYOMEVRHTJKSBDCCQQBFDBDSRJNRRI
OFJNHEWIVYMFAGGSWGTAWKDEKHMSIQZWWFEAXGANKEGOASNMGW
50
TTISKCFMCKNZPNTSOCSAXMJXVNQAZYXARANVCUNIFWKPIQJFNV
YLCVXBQGLTYDCLXTYTEOXCOZNOHEGUKKRNJHZJIBUJLGJLADZJ
50
TWUTSOFIUCTGSJGXIZALAHVRFHZRCXAUPFNMQSGOVPKIIYZJYK
ECXOMRXUXKPICDISAPMLDDNQTKOMNXMPFOLBXDBYDADSRLGOBU
50
KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK
LOWHDSQFDMNWHUWZZGCYRJHPGOPGXUANPXPSHBAYZCWOMPKWJX
50
ITMUSSMNFRPVJNBOIPQHCBWTAKULPROMCXHYPTLHWHEIQBIPFZ
TRLIKUOQUZWIDQCCOWBSNBUAPMTOGDNXAICMXMBPQHQZHOYPEF
50
YSSMABPEKNSAOJMMOIOPQOHIINEHOPJLHBQMGJRRLJDQIRGSXZ
ZPMXNOHQHSJIOEOLJSRBKIJBMPOSIMERJXIGQQALGHMPONDRAY
50
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
PTMBTCAKFLNBMADIQLFGBVJMPUIHYOJWGQNNVGLBVBVDSNQYMA
50
YALGFKKHAJFLJOAJGJNIIQMAGROGBADBBAAOFFPROJNMKBEAXZ
ZBGIPJJNIKFAFLMLJAAHFGAERBAOABOFNBKOXXJRJKMGGQDAOY
"""

from collections import Counter
def solve(A, B):
    L = len(A)
    acounters = []
    bcounters = []
    for i in range(1, L+1):
        for j in range(0, L-i+1):
            acounters.append(Counter(A[j:j+i]))
            bcounters.append(Counter(B[j:j+i]))
    c = 0
    for a in acounters:
        if a in bcounters:
            c += 1
    return c


data = large_input
As = data.splitlines()[3::3]
Bs = data.splitlines()[4::3]
with open("out/2018F-A.large.txt", "w") as f:
    for i, (A, B) in enumerate(zip(As, Bs)):
        t = "Case #%d: %d" %(i+1, solve(A, B))
        print(t)
        f.write(t)
        f.write("\n")




