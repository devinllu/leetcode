
def minWindow(s: str, t: str) -> str:

    lowest = ""
    res = ""
    min_length = float('inf')

    counter = {}
    for c in t:
        if c in counter.keys():
            counter[c] += 1
        else:
            counter[c] = 1

    for i in range(len(s)):
        d = counter.copy()
        print(d)
        for j in range(i, len(s)):
            c = s[j]
            lowest += c

            if c in d.keys():
                if d[c] != 0:
                    print(f'lowest: {lowest}, i: {i}')
                    d[c] -= 1
                    
            
            if all(val == 0 for val in d.values()):
                if len(lowest) < min_length:
                    min_length = len(lowest)
                    res = lowest
                lowest = ""
                break
    return res

print(minWindow("wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon", "ozgzyywxvtublcl"))