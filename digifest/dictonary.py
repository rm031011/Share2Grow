'''
positive_dict=['absolutely','accepted','acclaimed','accomplish','accomplishment','achievement','action','active','admire','adorable',
'adventure','affirmative','affluent','agree','agreeable','amazing','angelic','appealing','approve','aptitude','attractive','awesome','average',
'beaming','beautiful','believe','beneficial','bliss','bountiful','bounty','brave','bravo','bear','brilliant','bubbly','calm','celebrated',
'certain','champ','champion','charming','cheery','choice','classic','classical','clean','commend','composed','congratulation','constant',
'cool','courageous','creative','cute','dazzling','delight','delightful','divine','earnest','easy','ecstatic','effective',
'effervescent','efficient','effortless','electrifying','elegant','enchanting','encouraging','endorsed','energetic','energized','engaging',
'enthusiastic','essential','esteemed','ethical','excellent','exciting','exquisite','not','not worst',
'fabulous','fair','familiar','fantastic','favorable','fetching','fine','fitting','flourishing','fortunate','free','fresh','friendly',
'fun','generous','genius','genuine','giving','glamorous','glowing','good','gorgeous','graceful','great','green','grin','growing'
'handsome','happy','harmonious','healing','healthy','hearty','heavenly','honest','honorable','honored','hug','huge','idea','ideal','imaginative',
'imagine','impressive','independent','innovate','innovative','instant','instantaneous','instinctive','intellectual','intelligent',
'intuitive','inventive','jovial','joy','jubilant','keen','kind','knowing','knowledgeable','laugh','learned','legendary','light','lively',
'lovely','lucid','lucky','luminous','marvelous','masterful','meaningful','merit','meritorious','miraculous','motivating','moving',
'natural','nice','novel','now','nurturing','nutritious','okay','not bad','one','one-hundred percent','open','optimistic',
'paradise','perfect','phenomenal','pleasant','pleasurable','plentiful','poised','polished','popular','positive','powerful','prepared',
'pretty','principled','productive','progress','prominent','protected','proud','quality','quick','quiet','ready','reassuring','refined',
'refreshing','rejoice','reliable','remarkable','resounding','respected','restored','reward','rewarding','right','robust',
'safe','satisfactory','secure','seemly','simple','skilled','skillful','smile','soulful','sparkling','special','spirited','spiritual',
'stirring','stunning','stupendous','success','successful','sunny','super','superb','supporting','surprising',
'terrific','thorough','thrilling','thriving','tops','tranquil','transformative','transforming','trusting','truthful',
'unreal','unwavering','up','upbeat','upright','upstanding','valued','vibrant','victorious','victory','vigorous','virtuous','vital',
'vivacious','wealthy','welcome','well','whole','wholesome','willing','wonderful','wondrous','worthy','wow','yes','yummy','zeal','zealous']

positive_dict_syn=['incredible','unbelievable','improbable','astonishing','astounding','extraordinary',
'splendid','magnificent','comely','ravishing','aesthetic','pleasing','shapely','delicate','glorious','resplendent','radiant','blooming',
'fearless','dauntless','intrepid','plucky','daring','heroic','valorous','audacious','bold','gallant','valiant','doughty','mettlesome',
'bright','shining','shiny','gleaming','shimmering','vivid','colorful','lustrous','incandescent',
'quick-witted','smart','delicious','savory','delectable','appetizing','luscious','scrumptious',
'palatable','enjoyable','toothsome','enjoy','appreciate','delight in','be pleased','indulge in','luxuriate in','bask in','relish','devour','savor','like',
'famous','well-known','renowned','famed','eminent','illustrious','noted','notorious',
'funny','humorous','amusing','droll','comic','comical','laughable','silly',
'superior','qualified','suited','suitable','apt','proper','capable',
'kindly','gracious','obliging','agreeable','well-behaved','obedient', 
'trustworthy','profitable','advantageous','righteous','expedient','helpful','valid','ample','salubrious','estimable', 
'noble','first-rate','top-notch','sterling','respectable','edifying',
'noteworthy','distinguished','grand','considerable','much','mighty',
'mischievous','prankish','playful','naughty','roguish','waggish','impish','sportive',
'neat','orderly','tidy','trim','dapper','natty','well-organized','desirable','spruce','shipshape','well-kept',
'well-liked','approved','favorite','common','current']



negative_dict=['fedup','not good','not well','trounce','abysmal','adverseal','arming','angry','annoy','anxious','apathy','appalling','atrocious','awful',
'bad','banal','barbed','belligerent','bemoan','beneath','boring','broken','callous','cant','cannot','clumsy','coarse','cold','cold-hearted',
'collapse','confused','contradictory','contrary','corrosive','corrupt','crazy','creepy','criminal','cruel','cry','cutting',
'damage','damaging','dastardly','dead','decaying','deformed','deny','deplorable','depressed','deprived','despicable',
'detrimental','dirty','disease','disgusting','disheveled','dishonest','dishonorable','dismal','distress','dont','dreadful','dreary',
'enraged','eroding','evil','fail','faulty','fear','feeble','fight','filthy','foul','frighten','frightful',
'gawky','ghastly','grave','greed','grim','grimace','gross','grotesque','gruesome','guilty',
'haggard','hard','hard-hearted','harmful','hate','hideous','homely','horrendous','horrible','hostile','hurt','hurtful',
'icky','ignorant','ignore','ill','immature','imperfect','impossible','inane','inelegant','infernal','injure','injurious',
'insane','insidious','issue','insipid','jealous','junky','lose','lousy','lumpy','malicious','mean','menacing','messy','misshapen','missing',
'misunderstood','moan','moldy','monstrous','naive','nasty','naughty','negate','negative','never','no','nobody','nondescript',
'nonsense','not','noxious','objectionable','odious','offensive','old','oppressive','pain','perturb','pessimistic','petty',
'plain','poisonous','poor','prejudice','questionable','quirky','quit','problem',
'reject','renege','repellant','reptilian','repugnant','repulsive','revenge','revolting','rocky','rotten','rude','ruthless',
'sad','savage','scare','scary','scream','severe','shocking','shoddy','sick','sickening','sinister','slimy','smelly','sobbing',
'sorry','spiteful','sticky','stinky','stormy','stressful','stuck','stupid','substandard','suspect','suspicious',
'tense','terrible','terrifying','threatening','ugly','undermine','unfair','unfavorable','unhappy','unhealthy','unjust',
'unlucky','unpleasant','unsatisfactory','unsightly','untoward','unwanted','unwelcome','unwholesome','unwieldy','unwise','upset',
'vice','vicious','vile','villainous','vindictive','wary','weary','wicked','woeful','worthless','wound','worst'
'yell','yucky','zero']

'''

pos_dict_a=['absolutely', 'accepted', 'acclaimed', 'accomplish', 'accomplishment', 'achievement', 'action', 'active', 'admire', 'adorable', 'adventure', 'affirmative', 'affluent', 'agree', 'agreeable', 'amazing', 'angelic', 'appealing', 'approve', 'aptitude', 'attractive', 'awesome', 'average', 'astonishing', 'astounding', 'aesthetic', 'audacious', 'appetizing', 'appreciate', 'amusing', 'apt', 'agreeable', 'advantageous', 'ample', 'approved']
pos_dict_b=['beaming', 'beautiful', 'believe', 'beneficial', 'bliss', 'bountiful', 'bounty', 'brave', 'bravo', 'bear', 'brilliant', 'bubbly', 'blooming', 'bold', 'bright', 'be pleased', 'bask in']
pos_dict_c=['calm', 'celebrated', 'certain', 'champ', 'champion', 'charming', 'cheery', 'choice', 'classic', 'classical', 'clean', 'commend', 'composed', 'congratulation', 'constant', 'cool', 'courageous', 'creative', 'cute', 'comely', 'colorful', 'comic', 'comical', 'capable', 'considerable', 'common', 'current']
pos_dict_d=['dazzling', 'delight', 'delightful', 'divine', 'delicate', 'dauntless', 'daring', 'doughty', 'delicious', 'delectable', 'delight in', 'devour', 'droll', 'distinguished', 'dapper', 'desirable']
pos_dict_e=['earnest', 'easy', 'ecstatic', 'effective', 'effervescent', 'efficient', 'effortless', 'electrifying', 'elegant', 'enchanting', 'encouraging', 'endorsed', 'energetic', 'energized', 'engaging', 'enthusiastic', 'essential', 'esteemed', 'ethical', 'excellent', 'exciting', 'exquisite', 'extraordinary', 'enjoyable', 'enjoy', 'eminent', 'expedient', 'estimable', 'edifying']
pos_dict_f=['fabulous', 'fair', 'familiar', 'fantastic', 'favorable', 'fetching', 'fine', 'fitting', 'flourishing', 'fortunate', 'free', 'fresh', 'friendly', 'fun', 'fearless', 'famous', 'famed', 'funny', 'first-rate', 'favorite']
pos_dict_g=['generous', 'genius', 'genuine', 'giving', 'glamorous', 'glowing', 'good', 'gorgeous', 'graceful', 'great', 'green', 'grin', 'growinghandsome', 'glorious', 'gallant', 'gleaming', 'gracious', 'grand']
pos_dict_h=['happy', 'harmonious', 'healing', 'healthy', 'hearty', 'heavenly', 'honest', 'honorable', 'honored', 'hug', 'huge', 'heroic', 'humorous', 'helpful']
pos_dict_i=['idea', 'ideal', 'imaginative', 'imagine', 'impressive', 'independent', 'innovate', 'innovative', 'instant', 'instantaneous', 'instinctive', 'intellectual', 'intelligent', 'intuitive', 'inventive', 'incredible', 'improbable', 'intrepid', 'incandescent', 'indulge in', 'illustrious', 'impish']
pos_dict_j=['jovial', 'joy', 'jubilant']
pos_dict_k=['keen', 'kind', 'knowing', 'knowledgeable', 'kindly']
pos_dict_l=['laugh', 'learned', 'legendary', 'light', 'lively', 'lovely', 'lucid', 'lucky', 'luminous', 'lustrous', 'luscious', 'luxuriate in', 'like', 'laughable']
pos_dict_m=['marvelous', 'masterful', 'meaningful', 'merit', 'meritorious', 'miraculous', 'motivating', 'moving', 'magnificent', 'mettlesome', 'much', 'mighty', 'mischievous']
pos_dict_n=['not bad','not worst','natural', 'nice', 'novel', 'now', 'nurturing', 'nutritious', 'noted', 'notorious', 'noble', 'noteworthy', 'naughty', 'neat', 'natty']
pos_dict_o=['okay', 'one', 'one-hundred percent', 'open', 'optimistic', 'obliging', 'obedient', 'orderly']
pos_dict_p=['paradise', 'perfect', 'phenomenal', 'pleasant', 'pleasurable', 'plentiful', 'poised', 'polished', 'popular', 'positive', 'powerful', 'prepared', 'pretty', 'principled', 'productive', 'progress', 'prominent', 'protected', 'proud', 'pleasing', 'plucky', 'palatable', 'proper', 'profitable', 'prankish', 'playful']
pos_dict_q=['quality', 'quick', 'quiet', 'quick-witted', 'qualified']
pos_dict_r=['ready', 'reassuring', 'refined', 'refreshing', 'rejoice', 'reliable', 'remarkable', 'resounding', 'respected', 'restored', 'reward', 'rewarding', 'right', 'robust', 'ravishing', 'resplendent', 'radiant', 'relish', 'renowned', 'righteous', 'respectable', 'roguish']
pos_dict_s=['safe', 'satisfactory', 'secure', 'seemly', 'simple', 'skilled', 'skillful', 'smile', 'soulful', 'sparkling', 'special', 'spirited', 'spiritual', 'stirring', 'stunning', 'stupendous', 'success', 'successful', 'sunny', 'super', 'superb', 'supporting', 'surprising', 'splendid', 'shapely', 'shining', 'shiny', 'shimmering', 'smart', 'savory', 'scrumptious', 'savor', 'silly', 'superior', 'suited', 'suitable', 'salubrious', 'sterling', 'sportive', 'spruce', 'shipshape']
pos_dict_t=['terrific', 'thorough', 'thrilling', 'thriving', 'tops', 'tranquil', 'transformative', 'transforming', 'trusting', 'truthful', 'toothsome', 'trustworthy', 'top-notch', 'tidy', 'trim']
pos_dict_u=['unreal', 'unwavering', 'up', 'upbeat', 'upright', 'upstanding', 'unbelievable']
pos_dict_v=['valued', 'vibrant', 'victorious', 'victory', 'vigorous', 'virtuous', 'vital', 'vivacious', 'valorous', 'valiant', 'vivid', 'valid']
pos_dict_w=['wealthy', 'welcome', 'well', 'whole', 'wholesome', 'willing', 'wonderful', 'wondrous', 'worthy', 'wow', 'well-known', 'well-behaved', 'waggish', 'well-organized', 'well-kept', 'well-liked']
pos_dict_x=[]
pos_dict_y=['yes', 'yummy']
pos_dict_z=['zeal', 'zealous']



neg_dict_a=['abysmal', 'adverseal', 'arming', 'angry', 'annoy', 'anxious', 'apathy', 'appalling', 'atrocious', 'awful']
neg_dict_b=['bad', 'banal', 'barbed', 'belligerent', 'bemoan', 'beneath', 'boring', 'broken']
neg_dict_c=['callous', 'cant', 'cannot', 'clumsy', 'coarse', 'cold', 'cold-hearted', 'collapse', 'confused', 'contradictory', 'contrary', 'corrosive', 'corrupt', 'crazy', 'creepy', 'criminal', 'cruel', 'cry', 'cutting']
neg_dict_d=['damage', 'damaging', 'dastardly', 'dead', 'decaying', 'deformed', 'deny', 'deplorable', 'depressed', 'deprived', 'despicable', 'detrimental', 'dirty', 'disease', 'disgusting', 'disheveled', 'dishonest', 'dishonorable', 'dismal', 'distress', 'dont', 'dreadful', 'dreary']
neg_dict_e=['enraged', 'eroding', 'evil']
neg_dict_f=['fedup', 'fail', 'faulty', 'fear', 'feeble', 'fight', 'filthy', 'foul', 'frighten', 'frightful']
neg_dict_g=['gawky', 'ghastly', 'grave', 'greed', 'grim', 'grimace', 'gross', 'grotesque', 'gruesome', 'guilty']
neg_dict_h=['haggard', 'hard', 'hard-hearted', 'harmful', 'hate', 'hideous', 'homely', 'horrendous', 'horrible', 'hostile', 'hurt', 'hurtful']
neg_dict_i=['icky', 'ignorant', 'ignore', 'ill', 'immature', 'imperfect', 'impossible', 'inane', 'inelegant', 'infernal', 'injure', 'injurious', 'insane', 'insidious', 'issue', 'insipid']
neg_dict_j=['jealous', 'junky']
neg_dict_k=[]
neg_dict_l=['lose', 'lousy', 'lumpy']
neg_dict_m=['malicious', 'mean', 'menacing', 'messy', 'misshapen', 'missing', 'misunderstood', 'moan', 'moldy', 'monstrous']
neg_dict_n=['not good','naive', 'nasty', 'naughty', 'negate', 'negative', 'never', 'no', 'nobody', 'nondescript', 'nonsense', 'not', 'noxious']
neg_dict_o=['objectionable', 'odious', 'offensive', 'old', 'oppressive']
neg_dict_p=['pain', 'perturb', 'pessimistic', 'petty', 'plain', 'poisonous', 'poor', 'prejudice', 'problem']
neg_dict_q=['questionable', 'quirky', 'quit']
neg_dict_r=['reject', 'renege', 'repellant', 'reptilian', 'repugnant', 'repulsive', 'revenge', 'revolting', 'rocky', 'rotten', 'rude', 'ruthless']
neg_dict_s=['sad', 'savage', 'scare', 'scary', 'scream', 'severe', 'shocking', 'shoddy', 'sick', 'sickening', 'sinister', 'slimy', 'smelly', 'sobbing', 'sorry', 'spiteful', 'sticky', 'stinky', 'stormy', 'stressful', 'stuck', 'stupid', 'substandard', 'suspect', 'suspicious']	 	
neg_dict_t=['trounce', 'tense', 'terrible', 'terrifying', 'threatening']
neg_dict_u=['ugly', 'undermine', 'unfair', 'unfavorable', 'unhappy', 'unhealthy', 'unjust', 'unlucky', 'unpleasant', 'unsatisfactory', 'unsightly', 'untoward', 'unwanted', 'unwelcome', 'unwholesome', 'unwieldy', 'unwise', 'upset']
neg_dict_v=['vice', 'vicious', 'vile', 'villainous', 'vindictive']
neg_dict_w=['wary', 'weary', 'wicked', 'woeful', 'worthless', 'wound', 'worstyell']
neg_dict_x=[]
neg_dict_y=['yucky']
neg_dict_z=['zero']



