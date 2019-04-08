def count_vowels(str)
   str.to_enum(:scan, /[aeouiyAEOUIY]/).map { Regexp.last_match }.count
end

def find_next_hack_number(num)
  num += 1
    if check_for_hack_number(num)
        return num
    else
      find_next_hack_number(num)
  end
end