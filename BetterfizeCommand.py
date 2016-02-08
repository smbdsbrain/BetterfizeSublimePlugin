import sublime, sublime_plugin  
  
class BetterfizeCommand(sublime_plugin.TextCommand):  
    def run(self, view):  
                s = self.view.substr(self.view.sel()[0]) 
                i = 0
                while(i < len(s)):
                	if(s[i - 1] == '<' and s[i] == '/'):
                            print('found at', i)
                            j = 0
                            j = i
                            while(j < len(s) and s[j] != '>'):
                                j += 1

                            k = 0
                            k = j+1
                            while(k < len(s) and s[k] != '<'):
                                k += 1
                            m = 0
                            m = k + 1

                            while(m < len(s) and s[m] != '>'):
                                m += 1;

                            if(k < len(s) and m < len(s) and j < len(s) and s[i + 1 : j] ==  s[k+1:m] and s[i + 1 : j] != 'td'):
                                s = s[0:i - 1] + s[j + 1:k] + s[m + 1:len(s)]
                                i = 0
                        i += 1
                i = 0
                while(i < len(s)):
                        if(i > 6 and i < len(s) - 1 
                            and ((s[i] == ';' 
                            and s[i - 5: i + 1] != "&nbsp;" 
                            and s[i - 3: i + 1] != "&lt;"
                            and s[i - 3: i + 1] != "&gt;" 
                            and s[i - 6: i + 1] != "&Prime;" 
                            and s[i - 5: i + 1] != "&#010;"
                            and s[i - 5: i + 1] != "&#060;"
                            and s[i - 5: i + 1] != "&#062;"
                            and s[i - 5: i + 1] != "&#034;"
                            and s[i - 5: i + 1] != "&quot;"
                            and s[i - 4: i + 1] != "&amp;"
                            and s[i - 6: i + 1] != "&ndash;"
                            and s[i - 6: i + 1] != "&laquo;"
                            and s[i - 6: i + 1] != "&raquo;"
                            and s[i - 6: i + 1] != "&ldquo;"
                            and s[i - 6: i + 1] != "&rdquo;")
                            or s[i] == '{' or s[i] == '}'
                            or s[i - 4: i + 1] == "begin"
                            or s[i - 4: i + 1] == "BEGIN"
                            or s[i - 3: i + 1] == "then"
                            or s[i - 3: i + 1] == "else"
                            or s[i - 1: i + 1] == "do")
                            ):

                            s = s[0:i + 1] + "&#010;" + s[i + 1:len(s)];
                            i += 5
                        i += 1
                self.view.replace(view, self.view.sel()[0], s)


                




