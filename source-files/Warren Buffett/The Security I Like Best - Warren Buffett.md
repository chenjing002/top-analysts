# Warren E. Buffett — "The Security I Like Best"

**来源**：`Buffett-Old-invesetment-writeups-Commercial-_-Financial-Chronicle.pdf`（5 页扫描件，无文字层，300 dpi）。第 2–5 页页脚印有 "Digitized for FRASER — http://fraser.stlouisfed.org/"，即圣路易斯联储 FRASER 数字档案馆的扫描；第 1 页是单页重印本（"Reprinted from"），没有这个页脚。  
**出处**：*The Commercial and Financial Chronicle* 周刊专栏 "The Security I Like Best"  
**内容**：巴菲特在该专栏发表的 4 篇荐股文章全文逐字转录（PDF 第 3 页为同栏目另一作者 J. P. O'Rourke 的文章，不属巴菲特，未收录）

| # | 刊出日期 | 推荐标的 | 原刊页码 | PDF 页 |
| --- | --- | --- | --- | --- |
| 1 | 1951-12-06（周四） | Government Employees Insurance Co.（GEICO） | 重印本，未印页码 | 1 |
| 2 | 1953-04-09（周四） | Western Insurance Securities Co. 普通股 | Vol. 177, No. 5210, p. 2 (1522) | 2 |
| 3 | 1957-01-17（周四） | Oil and Gas Property Management, Inc. | p. 2 (198) | 5 |
| 4 | 1957-12-19（周四） | Home Protective Co. | p. 2 (2634) | 4 |

原刊页码取自各页页眉，括号内是全卷连续页码。1953 年那期的卷期号印在 PDF 第 3 页（同期第 43 页）页眉 "Volume 177 Number 5210 … (1563) 43"。两页的连续页码差 (1563 − 1522 = 41) 与刊内页码差 (43 − 2) 一致，可确认是同一期。1957-01-17 那期的 "(198)" 末位印刷模糊，也可能是 3。

## 转录与校对说明

- **方法**：从 PDF 提取原始 300 dpi 扫描图，逐栏裁切放大后用 Tesseract 出草稿，再逐行对照原图人工校正。OCR 误读的数字一律以原图为准；字形模糊的数字用像素级字形比对（与同页已知数字做相关性匹配）判定，并尽量用文中算术关系交叉验证。
- **忠实原文**：正文英文逐字保留原拼写和标点，包括 "Massachusett's"、"Best's aggregate's"、"acknowledgement" 等原文写法。排版断行处的连字符已合并（如 "pay-ments" 改为 "payments"）。照片图注（"Warren E. Buffett"）、广告和其他作者的文章不收录。"This Week's Forum Participants and Their Selections" 栏只保留巴菲特一条，同栏其他条目略去：1953-04 的 J. P. O'Rourke / Lloydminster Development，1957-01 的 Robert D. Tucker / Century Engineers，以及 1957-12 的 G. Shelby Friedrichs / Southdown Sugars。
- **段落与表格**：段落按原版分段。原版表格印在栏底，这里放在正文首次引用处（文中均以冒号或 "Table I below" 引出）。Oil and Gas 一文的储量表在原版中跨两栏印刷（左栏 Item / Gross Reserves，右栏 Net Reserve / Est'l. Gross Value），这里合并为一张表。
- **方括号 / 中文注**：凡方括号或中文括注均为整理者所加，不属于原文。
- **第二来源交叉核对**：拿另一份独立识别的版面解析 / OCR 结果 `Buffett-Old-invesetment-writeups-Commercial-_-Financial-Chronicle.pdf.json`，对第 1、2、4 篇做了全文逐词比对。该 JSON 只覆盖 PDF 第 1–4 页，**不含第 5 页**，所以 Oil and Gas 一文未经这一步。除断行连字符和粘连空格（如 "wereout"、"to3.0%"、"representsa"）外，共有 8 处不一致。逐一回到原图放大核查后，全部确认本转录正确、JSON 有误：

  | 位置 | JSON 识别 | 本转录（据原图） | 核查依据 |
  | --- | --- | --- | --- |
  | GEICO 增长表表头 | Year | Year— | 原图有破折号，与 Western Table I 的 "Years—" 同一体例 |
  | GEICO "1951 年上半年" 段 | Massachusetts | Massachusett's | 原图清晰可见撇号，属原文写法 |
  | Western 首段 | has naa price rise | has had a price rise | JSON 乱码 |
  | Western Table III 1949 年 Industry | 37.6% | 87.6% | 用 87.6 算五年均值为 92.58，与表中 "Average 92.6%" 吻合；用 37.6 则为 82.58 |
  | Western 倒数第 2 段（"The patient investor"） | arrears | arrearages | 原图断行为 "arrear-/ages" |
  | Home Protective 刊头年份 | 1937 | 1957 | 1937-12-19 为周日，1957-12-19 为周四；1937 年巴菲特才 7 岁 |
  | Home Protective "Dividends" 段 | rapsation | lapsation | JSON 误识首字母 |
  | Home Protective 表 1954 年 | 15.09 | 15.08 | 字形比对：与同表 "18.42" 中的 8 相关系数 0.73，高于与 "$9.92" 两个 9 的 0.69 / 0.44；末位左下笔画闭合，是 8 而非 9 |

  其余数字都与 JSON 的独立识别完全一致，包括 GEICO 1945 年保单持有人 51,697、Western 正文 $26,009,929 与 Table I 26,006,929 的前后差异，以及 Home Protective 1952 年 12.12、1956 年 22.62。这为下文"关键数字核对"多提供了一层独立印证。

### 原文排印问题（已核实，按原样保留）

1. **Western Insurance 1952 年保费前后不一致**：正文印作 **$26,009,929**，Table I 印作 **26,006,929**。两处都经放大和字形比对确认，属原版排印差异，各按原样转录。
2. **Western Insurance 表格错行**：原版 Table I 的百分比列、Table II 的 "Asset Value" 列、Table III 的 "Western Fire" 和 "Western Casualty" 两列，排版上都比年份列下移约一行。本转录按逻辑对齐，依据如下：Table I 的 "0.41 (Est.)" 只可能对应 1952；Table II 的 1952 年 86.26 与正文 "book value of $86.26" 一致；Table III 三列平均值经验算吻合（92.6 / 88.6 / 91.1）。
3. **Oil and Gas 一文刊头年份**：扫描件右上角把年份末位裁掉了（"January 17, 195_"）。1957-01-17 为周四，且文中引用 1955 年报、提及苏伊士局势，据此判定为 1957 年。

### 关键数字核对（附算术验证）

- GEICO：1945 年保单持有人 **51,697**（OCR 误读为 61,697，经字形比对确认首位为 5）；1949 年同业承保利润率 **6.7%**；1950 年末董事会 **16** 名成员（OCR 读作 10，此字略有破损，按 6 的开口和圆尾判定）。
- Western：$20,141,246 + $1,747,997 = $21,889,243，占比 92% / 8% ✓；Table II 1948 年每股收益 **$20.03**（非 20.08）；Table III 1949 年 Industry **87.6%**（五年均值验算吻合）。
- Home Protective：$1,100 × (3.60% − 2.04%) ≈ $17.2，与 "over $16 per share" 吻合 ✓；$1,100 × ½% = $5.50 ✓；调整后每股收益 1952 = **12.12**、1954 = **15.08**（JSON 识别为 15.09，见上表）、1956 = **22.62**。
- Oil and Gas：26,600,000 bbl × $2.75 = $73,150,000 ✓；199,800,000 MCF × $0.09 = $17,982,000 ✓；$49M − 超过 $33M = 不足 **$16M** ✓（OCR 误读为 $14）；毛储量 38,017,000 bbl × $0.50 ≈ $19M，约为 $5M 市值的 380%，即文中 "almost 400%" ✓。

---

## 1. Government Employees Insurance Co.（1951-12-06）

> Reprinted from *The Commercial and Financial Chronicle*, Thursday, December 6, 1951

**The Security I Like Best**

**WARREN E. BUFFETT**  
Buffett-Falk & Co., Omaha, Nebr.

**Government Employees Insurance Co.**

Full employment, boomtime profits and record dividend payments do not set the stage for depressed security prices. Most industries have been riding this wave of prosperity during the past five years with few ripples to disturb the tide.

The auto insurance business has not shared in the boom. After the staggering losses of the immediate postwar period, the situation began to right itself in 1949. In 1950, stock casualty companies again took it on the chin with underwriting experience the second worst in 15 years. The recent earnings reports of casualty companies, particularly those with the bulk of writings in auto lines, have diverted bull market enthusiasm from their stocks. On the basis of normal earning power and asset factors, many of these stocks appear undervalued.

The nature of the industry is such as to ease cyclical bumps. Auto insurance is regarded as a necessity by the majority of purchasers. Contracts must be renewed yearly at rates based upon experience. The lag of rates behind costs, although detrimental in a period of rising prices as has characterized the 1945-1951 period, should prove beneficial if deflationary forces should be set in action.

Other industry advantages include lack of inventory, collection, labor and raw material problems. The hazard of product obsolescence and related equipment obsolescence is also absent.

Government Employees Insurance Corporation was organized in the mid-30's to provide complete auto insurance on a nationwide basis to an eligible class including: (1) Federal, State and municipal government employees; (2) active and reserve commissioned officers and the first three pay grades of non-commissioned officers of the Armed Forces; (3) veterans who were eligible when on active duty; (4) former policyholders; (5) faculty members of universities, colleges and schools; (6) government contractor employees engaged in defense work exclusively, and (7) stockholders.

The company has no agents or branch offices. As a result, policyholders receive standard auto insurance policies at premium discounts running as high as 30% off manual rates. Claims are handled promptly through approximately 500 representatives throughout the country.

The term "growth company" has been applied with abandon during the past few years to companies whose sales increases represented little more than inflation of prices and general easing of business competition. GEICO qualifies as a legitimate growth company based upon the following record:

| Year— | Premiums Written | Policyholders |
| --- | ---: | ---: |
| 1936 | $103,696.31 | 3,754 |
| 1940 | 768,057.86 | 25,514 |
| 1945 | 1,638,562.09 | 51,697 |
| 1950 | 8,016,975.79 | 143,944 |

Of course the investor of today does not profit from yesterday's growth. In GEICO's case, there is reason to believe the major portion of growth lies ahead. Prior to 1950, the company was only licensed in 15 of 50 jurisdictions including D. C. and Hawaii. At the beginning of the year there were less than 3,000 policyholders in New York State. Yet 25% saved on an insurance bill of $125 in New York should look bigger to the prospect than the 25% saved on the $50 rate in more sparsely settled regions.

As cost competition increases in importance during times of recession, GEICO's rate attraction should become even more effective in diverting business from the brother-in-law. With insurance rates moving higher due to inflation, the 25% spread in rates becomes wider in terms of dollars and cents.

There is no pressure from agents to accept questionable applicants or renew poor risks. In States where the rate structure is inadequate, new promotion may be halted.

Probably the biggest attraction of GEICO is the profit margin advantage it enjoys. The ratio of underwriting profit to premiums earned in 1949 was 27.5% for GEICO as compared to 6.7% for the 135 stock casualty and surety companies summarized by Best's. As experience turned for the worse in 1950, Best's aggregate's profit margin dropped to 3.0% and GEICO's dropped to 18.0%. GEICO does not write all casualty lines; however, bodily injury and property damage, both important lines for GEICO, were among the least profitable lines. GEICO also does a large amount of collision writing, which was a profitable line in 1950.

During the first half of 1951, practically all insurers operated in the red on casualty lines with bodily injury and property damage among the most unprofitable. Whereas GEICO's profit margin was cut to slightly above 9%, Massachusett's Bonding & Insurance showed a 16% loss, New Amsterdam Casualty an 8% loss, Standard Accident Insurance a 9% loss, etc.

Because of the rapid growth of GEICO, cash dividends have had to remain low. Stock dividends and a 25-for-1 split increased the outstanding shares from 3,000 on June 1, 1948, to 250,000 on Nov. 10, 1951. Valuable rights to subscribe to stock of affiliated companies have also been issued.

Benjamin Graham has been Chairman of the Board since his investment trust acquired and distributed a large block of the stock in 1948. Leo Goodwin, who has guided GEICO's growth since inception, is the able President. At the end of 1950, the 16 members of the Board of Directors owned approximately one-third of the outstanding stock.

Earnings in 1950 amounted to $3.92 as contrasted to $4.71 on the smaller amount of business in 1949. These figures include no allowance for the increase in the unearned premium reserve which was substantial in both years. Earnings in 1951 will be lower than 1950, but the wave of rate increases during the past summer should evidence themselves in 1952 earnings. Investment income quadrupled between 1947 and 1950, reflecting the growth of the company's assets.

At the present price of about eight times the earnings of 1950, a poor year for the industry, it appears that no price is being paid for the tremendous growth potential of the company.

*This is part of a continuous forum appearing in the "Chronicle," in which each week, a different group of experts in the investment and advisory field from all sections of the country participate and give their reasons for favoring a particular security.*

---

## 2. Western Insurance Securities Co.（1953-04-09）

> *The Commercial and Financial Chronicle* . . . Thursday, April 9, 1953
>
> **The Security I Like Best** — A continuous forum in which, each week, a different group of experts in the investment and advisory field from all sections of the country participate and give their reasons for favoring a particular security.
>
> (The articles contained in this forum are not intended to be, nor are they to be regarded, as an offer to sell the securities discussed.)
>
> [This Week's Forum Participants and Their Selections] Western Insurance Securities Co.—Warren E. Buffett, Buffett-Falk & Co., Omaha, Neb. (P. 2)

**WARREN E. BUFFETT**  
Buffett-Falk & Co., Omaha, Nebr.

**Western Insurance Securities**  
**Common Stock**

Again my favorite security is the equity stock of a young, rapidly growing and ably managed insurance company. Although Government Employees Insurance Co., my selection of 15 months ago, has had a price rise of more than 100%, it still appears very attractive as a vehicle for long-term capital growth.

Rarely is an investor offered the opportunity to participate in the growth of two excellently managed and expanding insurance companies on the grossly undervalued basis which appears possible in the case of the Western Insurance Securities Company. The two operating subsidiaries, Western Casualty & Surety, and Western Fire, wrote a premium volume of $26,009,929 in 1952 on consolidated admitted assets of $29,590,142. Now licensed in 38 states, their impressive growth record, both absolutely and relative to the industry, is summarized in Table I below.

**TABLE I**

| Years— | Average Premium Volume Western Insurance | Percent of Total Stock Fire & Casualty Premiums |
| --- | ---: | ---: |
| 1924-30 | $838,860 | 0.05% |
| 1931-35 | 2,667,003 | 0.20 |
| 1936-40 | 3,955,403 | 0.25 |
| 1941-45 | 5,023,219 | 0.24 |
| 1946-50 | 13,959,506 | 0.33 |
| 1951 | 22,055,001 | 0.38 |
| 1952 | 26,006,929 | 0.41 (Est.) |

Western Insurance Securities owns 92% of Western Casualty and Surety, which in turn owns 99.95% of Western Fire Insurance. Other assets of Western Insurance Securities are minor, consisting of approximately $180,000 in net quick assets. The capitalization consists of 7,000 shares of $100 par 6% preferred, callable at $125; 35,000 shares of Class A preferred, callable at $60, which is entitled to a $2.50 regular dividend and participates further up to a maximum total of $4 per share; and 50,000 shares of common stock. The arrears on the Class A presently amount to $36.75.

The management headed by Ray DuBoc is of the highest grade. Mr. DuBoc has ably steered the company since its inception in 1924 and has a reputation in the insurance industry of being a man of outstanding integrity and ability. The second tier of executives is also of top caliber.

During the formative years of the company, senior charges were out of line with the earning power of the enterprise. The reader can clearly perceive why the same senior charges that caused such great difficulty when premium volume ranged about the $3,000,000 mark would cause little trouble upon the attainment of premium volume in excess of $26,000,000.

Adjusting for only 25% of the increase in the unearned premium reserve, earnings of $1,367,063 in 1952, a very depressed year for auto insurers, were sufficient to cover total senior charges of $129,500 more than 10 times over, leaving earnings of $24.74 on each share of common stock.

It is quite evident that the common stock has finally arrived, although investors do not appear to realize it since the stock is quoted at less than twice earnings and at a discount of approximately 55% from the December 31, 1952, book value of $86.26 per share. Table II indicates the postwar record of earnings and dramatically illustrates the benefits being realized by the common stock because of the expanded earnings base. The book value is calculated with allowance for a 25% equity in the unearned premium reserve and is after allowance for call price plus arrears on the preferreds:

**TABLE II**

| Year | Common Stock Earnings | Asset Value |
| --- | ---: | ---: |
| 1948 | $20.03 | ($0.41) |
| 1949 | 21.66 | 21.25 |
| 1950 | 23.64 | 44.90 |
| 1951 | 16.61 | 61.50 |
| 1952 | 24.74 | 86.26 |

Since Western has achieved such an excellent record in increasing its industry share of premium volume, the reader may well wonder whether underwriting standards have been compromised. This is definitely not the case. During the past ten years Western's operating ratios have proved quite superior to the average multiple line company. The combined loss and expense ratios for the two Western companies as reported by the Alfred M. Best Co. on a case basis are compared in Table III with similar ratios for all stock fire and casualty companies:

**TABLE III**

| Year | Industry | Western Fire | Western Casualty |
| --- | ---: | ---: | ---: |
| 1948 | 91.2% | 90.1% | 74.6% |
| 1949 | 87.6% | 84.2% | 92.4% |
| 1950 | 93.0% | 85.6% | 90.7% |
| 1951 | 97.1% | 91.2% | 101.1% |
| 1952 | 94.0% (Est.) | 91.8% | 96.7% |
| Average | 92.6% | 88.6% | 91.1% |

The careful reader will not overlook the possibility that Western's superior performance has been due to a concentration of writings in unusually profitable lines. Actually the reverse is true. Although represented in all major lines, Western is still primarily an automobile insurer with 60% of its volume derived from auto lines. Since automobile underwriting has proven generally unsatisfactory in the postwar period, and particularly so in the last three years, Western's experience was even more favorable relative to the industry than the tabular comparison would indicate.

Western has always maintained ample loss reserves on unsettled claims. Underwriting results in the postwar period have shown Western to be over-reserved at the end of each year. Triennial examinations conducted by the insurance commissioners have confirmed these findings.

Turning to their investment picture, we of course find a growth in invested assets and investment income paralleling the growth in premium volume. Consolidated net assets have risen from $5,154,367 in 1940 to their present level of $29,590,142. Western follows an extremely conservative investment policy, relying upon growth in premium volume for expansion in investment income. Of the year-end portfolio of $21,889,243, governments plus a list of well diversified high quality municipals total $20,141,246 or 92% and stocks only $1,747,997 or 8%. Net investment income of $474,472 in 1952 was equal to $6.14 per share of Western Insurance common after minority interest and assuming senior charges were covered entirely from investment income.

The casualty insurance industry during the past several years has suffered staggering losses on automobile insurance lines. This trend was sharply reversed during late 1952. Substantial rate increases in 1951 and 1952 are being brought to bear on underwriting results with increasing force as policies are renewed at much higher premiums. Earnings within the casualty industry are expected to be on a very satisfactory basis in 1953 and 1954.

Western, while operating very profitably during the entire trying period, may be expected to report increased earnings as a result of expanding premium volume, increased assets, and the higher rate structure. An earned premium volume of $30,000,000 may be conservatively expected by 1954. Normal earning power on this volume should average about $30.00 per share, with investment income contributing approximately $8.40 per share after deducting all senior charges from investment income.

The patient investor in Western Insurance common can be reasonably assured of a tangible acknowledgement of his enormously strengthened equity position. It is well to bear in mind that the operating companies have expanded premium volume some 550% in the last 12 years. This has required an increase in surplus of 350% and consequently restricted the payment of dividends. Recent dividend increases by Western Casualty should pave the way for more prompt payment on arrearages. Any leveling off of premium volume will permit more liberal dividends while a continuation of the past rate of increase, which in my opinion is very unlikely, would of course make for much greater earnings.

Operating in a stable industry with an excellent record of growth and profitability, I believe Western Insurance common to be an outstanding vehicle for substantial capital appreciation at its present price of about 40. The stock is traded over-the-counter.

*Continued on page 43*（原版排版标记：指本栏目下一位作者 J. P. O'Rourke 的文章接续至第 43 页，即本 PDF 第 3 页；巴菲特本文在此已完整结束。）

---

## 3. Oil and Gas Property Management, Inc.（1957-01-17）

> *The Commercial and Financial Chronicle* . . . Thursday, January 17, 195[7]
>
> **The Security I Like Best** — A continuous forum in which, each week, a different group of experts in the investment and advisory field from all sections of the country participate and give their reasons for favoring a particular security.
>
> (The articles contained in this forum are not intended to be, nor are they to be regarded, as an offer to sell the securities discussed.)
>
> [This Week's Forum Participants and Their Selections] Oil and Gas Property Management, Inc.—Warren E. Buffett, Manager, General Private Investment Groups, Omaha, Neb. (Page 2)

**WARREN E. BUFFETT**  
Manager, Several Private Investment Groups, Omaha, Neb.

**Oil and Gas Property Management, Inc.**

A more fitting title for my selection would be "The Inflation Hedge I Like Best." Should inflation continue O & G may well be the vehicle to give the investor the same supercharged performance that highly leveraged investment trusts and warrants did in the early 40's.

O & G was organized in 1953 by interests affiliated with the Empire Trust to buy and manage producing oil and gas properties. The management is of the highest caliber and the Empire's reputation and experience in oil matters has undoubtedly been of considerable value. Purchases have been made subject to substantial oil payments with a large portion of income in early years used to extinguish these payments. This method might be compared to real estate purchased subject to large mortgages with rental income, exclusive of that portion needed for operating expenses, utilized for mortgage reduction. The tax laws facilitate this method very considerably when applied to oil by allowing all payments as a direct exclusion from income. Accounting-wise, the result is to show a very small gross income while the equity is being built up substantially. Accordingly, the financial services do not show accurately the operating picture of O & G and the interested reader should study the annual reports of the company.

The equity money for O & G was originally raised by the sale of $10 million income debentures with 300,000 shares of stock attached. This issue was exceptionally well placed in large blocks with Wall Street houses, investment trusts, etc. The underwriting fee on the sale amounted to about ¼ of 1%. An additional 80,000 shares of common were sold to the promoting group with the Empire Trust reputedly owning over 50,000 shares in a subsidiary. Large issues of warrants and options are conspicuous by their absence.

The equity money of O & G was invested by the end of 1954. Thus the company has acquired its properties on a somewhat more reasonable basis than might be expected at current higher prices for oil in the ground.

The table below shows the substantial reserves of the company and illustrates the dynamic possibilities of the small issue of common stock even should no increase in oil and gas prices occur. Figures are based on the 1955 annual report and we understand there has been little change since that date.

| Item | Gross Reserves | Net Reserve for Stk. & Debs. | Est'l. Gross Value of Net Reserves |
| --- | ---: | ---: | ---: |
| Oil & Plant Products | 38,017,000 bbls. | 26,600,000 bbls. | $73,150,000 ($2.75 bbl.) |
| Gas | 500,957,000 MCF | 199,800,000 MCF | $17,982,000 (9¢ MCF) |

The net reserves for stock and debentures reflect the reduction from gross reserves of amounts sufficient to retire oil payments and loans. The debentures are income bonds and are not expected to pay their interest (which cumulates) until most of the oil payments have been liquidated. Accordingly, it may be estimated that approximately $15 million will be required to retire the debentures with interest. Operating expenses of course must be deducted from the gross values in the last column of the table and in the case of plant products, which represent half the oil reserves, will be more than average. Allowing $35 million for operating expenses and possible taxes still leaves a potential for the common of $40 million. Future acquisitions could increase this substantially.

The 380,000 shares of common have a total market value of about $5 million which makes the arithmetic of the picture fascinating. An increase in the price of oil of 15 cents per barrel or 1 cent per MCF in the case of gas is equal to the entire market value of the common. If oil over the next few years were to increase in price 50 cents per barrel, the gain in value would be equal to almost 400% of the current total market price of the common.

At the end of 1955 the company had about $49 million of oil payments and about $17 million of loans and debentures ahead of the 380,000 shares of common. However, over $33 million of the payments is applicable to one property and it is important to note that payments are obligations of only the specific property, not the company. The balance of payments amounted to less than $16 million and were reduced by $4 million in 1955 alone. Currently the average payout on these is probably less than three years away.

It is interesting to compare O & G with its more well known counterpart — Producing Properties, Inc. This company also started with about $10 million of equity capital although it didn't get under way until early 1955. At a recent date PP's production was running about 2,200 barrels per day against over 7,000 for O & G and their net reserves were also less than a third those of O & G. On the other hand, they had invested only about half of their equity money so it is not to be implied that they were doing a poorer job of investing the money—it is just that they got off to a later start. However, PP common is selling in the market for about $14 million and, in our opinion, represents less value and potential than is present in O & G selling for $5 million. If O & G were to command only the same valuation, it would mean a price of over $35 per share.

O & G also owns a half interest in Yemen Development Corp. which holds a concession on two-thirds of Yemen covering 40,000 square miles including a large basin area. Geological reports are favorable although Suez unrest will undoubtedly delay testing this area. Offsetting this plus potential in the picture is a minus potential in that the largest property of O & G is involved in litigation concerning gas prices. O & G's position has been upheld by the FPC; however, the matter is now before the courts.

O & G common, selling around 14 in the Over-the-Counter Market, should do very well if present oil prices are maintained and presents outstanding possibilities should inflation continue. Behind $65 million of obligations with an estimated gross value of oil and gas offsetting these obligations of $150 million, the $5 million market valuation on the common seems to offer considerably higher chances for gain than for loss. A small investment in O & G should do the job that a many times larger investment in a non-leveraged oil holding would do while exposing the holder to a much smaller maximum loss.

---

## 4. Home Protective Co.（1957-12-19）

> *The Commercial and Financial Chronicle* . . . Thursday, December 19, 1957
>
> **The Security I Like Best** — A continuous forum in which, each week, a different group of experts in the investment and advisory field from all sections of the country participate and give their reasons for favoring a particular security.
>
> (The articles contained in this forum are not intended to be, nor are they to be regarded, as an offer to sell the securities discussed.)
>
> [This Week's Forum Participants and Their Selections] Home Protective Company—Warren E. Buffett, Manager — Several Private Investment Groups, Omaha, Neb. (Page 2).

**WARREN E. BUFFETT**  
Manager—Several Private Investment Groups  
Omaha, Nebr.

**HOME PROTECTIVE CO.**  
(A Life Insurance Stock)

Home Protective Co. probably represents the last "undiscovered" equity security of a major life insurance company. This lack of investor awareness causes the security to sell at less than half of the lowest price-earnings ratio placed on comparable companies. Home Protective is currently selling at less than four times earnings. Any education of investors to the facts concerning the company should result in a substantially higher appraisal.

Home Protective has only 61,463 shares of stock outstanding. The company owns 98½% of the outstanding stock of the Home Life Insurance Co. of America, a leading Pennsylvania insurer with over 400,000 policyholders. After allowing for inter-company items, Home Protective has very little in the way of other assets and liabilities. As a practical matter, with only 1½% of the stock of Home Life held by others, Home Protective Co. is the Home Life Insurance Co. of America from a stockholder standpoint.

Whereas some years back the company had a very dubious financial position, strict adherence to the highest standards of investment in the placement of new funds plus utilization of retained earnings in very substantial charges against over-valued assets have given Home a very strong financial picture. While in 1946 government-guaranteed mortgages only accounted for about 13% of assets, they now represent over 50% of assets which is greatly above the industry average. During the same period the average rate earned on assets has increased from 2.04% to 3.60%. This gain based on present assets of $1,100 per share amounts to over $16 per share annually.

Home's business is entirely non-participating. The stockholder need make no guesses as to what belongs to him and what really belongs to the policyholder. Currently Home has close to $300 million of insurance in force with practically no low-profit group. The business is almost entirely ordinary and industrial with the latter fully as profitable as the former. The lapse ratio of the company has been very low indicating well-seasoned business and experienced mortality has been excellent.

Dividends have been small while the company has been writing down assets to realistic values and the 50-cent annual rate will probably be continued for some years while the capital base is enlarged in line with the amount of business on the books. However, the earnings power has been maintaining a steady march upward and with a continuation of higher yields, low lapsation and favorable mortality, a greater base of business should create further increases in earnings. With each share of Home Protective representing $1,100 in assets, a ½ of 1% change in interest rates represents a $5.50 per share change in earning power. While it takes considerable time to be fully effective, we have witnessed such a change within the past year and it has not yet been reflected in Home's earnings.

The company possesses an additional "kicker" in large holdings of contiguous undeveloped land on the Main Line in Philadelphia. Given proper zoning such holdings can have substantially greater value, particularly when related to only 61,463 shares outstanding.

Adjusting for changes in insurance in force at conservative rates, the following earnings are indicated for the past six years:

| Year | Adjusted Earnings per Share |
| --- | ---: |
| 1951 | $9.92 |
| 1952 | 12.12 |
| 1953 | 12.25 |
| 1954 | 15.08 |
| 1955 | 18.42 |
| 1956 | 22.62 |

A continuation of such increases which appears likely added to greater investor recognition should provide substantial capital gains to today's buyer at the 85 level in the Over-the-Counter market.
