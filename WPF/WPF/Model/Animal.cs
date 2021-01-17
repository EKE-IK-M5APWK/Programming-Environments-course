using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace WPF.Model
{
    public class Animal
    {

        [JsonProperty(PropertyName = "Name")]
        public string Name
        {
            get;
            set;
        }
        
        [JsonProperty(PropertyName = "Age")]
        public int Age
        {
            get;
            set;
        }
        
        [JsonProperty(PropertyName = "Species")]
        public string Species
        {
            get;
            set;
        }
        [JsonProperty(PropertyName = "Breed")]
        public string Breed
        {
            get;
            set;
        }
        
        [JsonProperty(PropertyName = "Color")]
        public string Color
        {
           get;
           set;
        }
        
        [JsonProperty(PropertyName = "Height")]
        public double Height
        {
           get;
           set;
        }
        
        [JsonProperty(PropertyName = "Weight")]
        public double Weight
        {
            get;
            set;
        }
        
        [JsonProperty(PropertyName = "Sex")]
        public Sex Sex
        {
            get;
            set;
        }
        
        [JsonProperty(PropertyName = "Condition")]
        public StateOfCondition Condition
        {
            get;
            set;
        }
        
         [JsonProperty(PropertyName = "Adpoted")]
        public Adopted Adopted
        {
            get;
            set;
        }

        public Sex getSex()
        {
            return this.Sex;
        }
    }
    public enum Sex
    {
        Male = 0,
        Female = 1
    }
    public enum Adopted
    {
        Igen = 0,
        Nem = 1
    }
    public enum StateOfCondition
    {
        Well = 0,
        Sick = 1,
        Rehabilitation = 2
    }
    
}

